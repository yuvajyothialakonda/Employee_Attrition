import os
import joblib
import streamlit as st

# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build full path to model file
model_path = os.path.join(BASE_DIR, "attrition_model.pkl")

# Check if file exists before loading
if not os.path.exists(model_path):
    st.error(f"Model file not found at: {model_path}")
    st.stop()

# Load the model safely
model = joblib.load(model_path)

# ------------------- UI -------------------

st.title("Employee Attrition Prediction")

st.write("Enter employee details:")

age = st.number_input("Age", min_value=18, max_value=60)
salary = st.number_input("Monthly Income", min_value=1000, max_value=100000)
years = st.number_input("Years at Company", min_value=0, max_value=40)

# Predict button
if st.button("Predict"):
    # Example input format (adjust based on your model)
    input_data = [[age, salary, years]]

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Employee likely to leave")
    else:
        st.success("✅ Employee likely to stay")