# Sentiment-Analysis

Welcome to the Sentiment Analysis Web Application! This project provides a straightforward tool for analyzing text sentiment using machine learning models. Whether you're interested in how various texts are perceived or looking to incorporate sentiment analysis into your projects, this tool offers simplicity and effectiveness.

## ✨ Features
- **Model Selection**: Choose between Logistic Regression or Neural Network models.
- **Instant Sentiment Analysis**: Get immediate feedback on whether your text is positive or negative.
- **User-Friendly Interface**: Enjoy a clean and intuitive design for easy navigation.

## 🔧 Technology Stack
- **Backend**: Flask
- **Machine Learning**: Scikit-Learn
- **Frontend**: HTML, CSS
- **Data Handling**: Joblib for model and vectorizer serialization

## 🚀 Installation

To set up and run this project locally, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/Sentiment-Analysis-Web-App.git
    cd Sentiment-Analysis-Web-App
    ```

2. **Set Up a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download Models and Vectorizer:**

    Ensure you have the pre-trained models (`logistic_model.pkl`, `mlp_model.pkl`) and vectorizer (`vectorizer.pkl`) in the project directory.

5. **Run the Application:**

    ```bash
    python app.py
    ```

6. **Access the Application:**

    Open your web browser and go to `http://127.0.0.1:5000/` to start using the app.

## 🔍 Usage

1. **Select a Model:** Choose between Logistic Regression or Neural Network from the dropdown menu.
2. **Enter Text:** Type the text you want to analyze.
3. **Click "Analyze Sentiment":** Receive the sentiment analysis result instantly.

## 📈 Example Output

- **Model Used**: Neural Network
- **Sentiment**: Negative

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Make your changes and commit: `git commit -am 'Add new feature'`
4. Push the branch: `git push origin feature/YourFeature`
5. Open a pull request.

Thank you for exploring this project! We hope it serves your sentiment analysis needs well. 🎉

---

Feel free to modify any section to better fit your project’s details or personal style!
