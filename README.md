# Iris Flower Classification 🌸

## Project Overview
This project predicts the species of an Iris flower based on its sepal and petal measurements using machine learning. A Streamlit web application allows users to enter measurements and view predictions.

## Problem Statement
Classify an Iris flower into one of three species:
- Setosa
- Versicolor
- Virginica

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

## Project Workflow
1. Load the Iris dataset.
2. Explore and analyze the data.
3. Split the data into training and testing sets.
4. Train and compare classification models.
5. Evaluate model performance.
6. Save the selected model.
7. Build a Streamlit web application for predictions.

## Features
- Accepts four flower measurements.
- Predicts the flower species.
- Displays prediction probabilities when supported by the selected model.

## Live Demo

Try the Iris Flower Classification app online:

[Open Live App](https://iris-flower-classification-wasim.streamlit.app)

## Project Files
- `app.py` — Streamlit application.
- `iris_model.joblib` — Saved machine learning model.
- `iris_classification.ipynb` — Notebook containing analysis and model development.

## Installation

Install the required libraries:

```bash
pip install streamlit pandas scikit-learn joblib
```

## Run the Application

Make sure `app.py` and `iris_model.joblib` are in the same folder, then run:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## Dataset
The project uses the Iris dataset available through Scikit-learn.

## Learning Outcomes
- Data exploration and preprocessing
- Classification model training
- Model evaluation
- Model saving and loading
- Building a web app with Streamlit

## Author
Created as a machine learning learning project.
