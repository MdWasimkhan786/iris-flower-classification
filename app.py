
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Iris Flower Classifier",
    page_icon="🌸"
)

model_path = Path(__file__).parent / "iris_model.joblib"
model = joblib.load(model_path)

species_names = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

st.title("🌸 Iris Flower Classification")
st.write("Enter flower measurements below.")

sepal_length = st.number_input(
    "Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1
)
sepal_width = st.number_input(
    "Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5
)
petal_length = st.number_input(
    "Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4
)
petal_width = st.number_input(
    "Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2
)

if st.button("Predict Species"):
    flower = pd.DataFrame([{
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }])

    prediction = int(model.predict(flower)[0])
    st.success(f"Predicted Species: {species_names[prediction]}")
