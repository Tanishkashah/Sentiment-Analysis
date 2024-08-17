# Sentiment Analysis Project

## Overview
This project aims to classify movie reviews as positive or negative using two different machine learning models: **Logistic Regression** and **Multi-Layer Perceptron (MLP) Classifier**. The models are built and evaluated using a publicly available dataset of movie reviews.

## Table of Contents
1. [Task Overview and Problem Statement](#task-overview-and-problem-statement)
2. [Dataset](#dataset)
3. [Data Preprocessing](#data-preprocessing)
4. [Model Building](#model-building)
5. [Model Training and Evaluation](#model-training-and-evaluation)
6. [Insights And Observations](#insights-and-observations)
7. [Conclusion](#conclusion)
8. [Files Included](#files-included)

## Task Overview and Problem Statement
The goal of this project is to develop a sentiment analysis model that can accurately classify movie reviews as either positive or negative. This is achieved by leveraging two different modeling approaches: Logistic Regression and MLP Classifier.

## Dataset
The dataset used for this project is the IMDb dataset, which contains 50,000 movie reviews labeled as positive or negative. The dataset is publicly available and can be accessed [here](https://ai.stanford.edu/~amaas/data/sentiment/).

## Data Preprocessing
Data preprocessing steps include:
- Lowercasing the text
- Tokenization
- Removing punctuation and stopwords
- Stemming/Lemmatization
- Vectorization using TF-IDF

## Model Building
Two models were built for this project:
1. **Logistic Regression**: A simple and interpretable model for binary classification.
2. **MLP Classifier**: A neural network model capable of capturing complex patterns in the data.

## Model Training and Evaluation
Both models were trained on the preprocessed dataset and evaluated using metrics such as accuracy, precision, recall, and F1-score. The evaluation results are compared to determine the effectiveness of each model.

## Insights And Observations
- The MLP Classifier generally outperformed Logistic Regression in terms of accuracy and F1-score.
- Logistic Regression provided a strong baseline due to its simplicity and interpretability.

## Conclusion
This project demonstrated the effectiveness of both Logistic Regression and MLP Classifier for sentiment analysis. While the MLP Classifier showed better performance, Logistic Regression remains a valuable tool for simpler tasks.

## Files Included
- `ML-modelling.ipynb`: Jupyter notebook containing the implementation of Logistic Regression and MLP Classifier.
- `lstm.ipynb`: (If applicable) Jupyter notebook for LSTM model implementation (not used in this project).

## Installation
To run this project, ensure you have the following libraries installed:
```bash
pip install pandas numpy scikit-learn
