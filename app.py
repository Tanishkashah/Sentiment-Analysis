from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask import render_template

app = Flask(__name__)

# Load the models and vectorizer

logistic_model = joblib.load('log_reg.pkl')

mlp_model = joblib.load('nn.pkl')

vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # Ensure index.html is in the templates folder

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    text = data['text']
    model_choice = data['model']
    
    # Transform the input text
    X = vectorizer.transform([text])
    
    # Get predictions based on chosen model
    if model_choice == 'logistic_regression':
        prediction = logistic_model.predict(X)[0]
    elif model_choice == 'neural_network':
        prediction = mlp_model.predict(X)[0]
    else:
        return jsonify({'error': 'Invalid model choice'})
    
    return jsonify({
        'prediction': prediction
    })

if __name__ == '__main__':
    app.run(debug=True)
