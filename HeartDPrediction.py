import streamlit as st
import pickle
import pandas as pd
import os

# Check if the model file exists
model_path = r'C:\Users\suyas\OneDrive\Documents\Heart Diesease prediction\random_forest_model.pkl'

if not os.path.exists(model_path):
    st.error(f"Model file not found at {model_path}. Please check the file path.")
else:
    try:
        # Load the model
        with open(model_path, 'rb') as file:
            rf_model = pickle.load(file)
    except Exception as e:
        st.error(f"Error loading the model: {e}")

# App title
st.title("Heart Disease Prediction App")

# Collect user inputs
age = st.number_input("Age", min_value=0, max_value=120, value=30)
sex = st.selectbox("Sex (1=Male, 0=Female)", options=[1, 0])
cp = st.selectbox("Chest Pain Type (0, 1, 2, 3)", options=[0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", min_value=0, max_value=200, value=120)
chol = st.number_input("Cholesterol", min_value=0, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1=Yes, 0=No)", options=[1, 0])
restecg = st.selectbox("Resting ECG Results (0, 1, 2)", options=[0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=300, value=150)
exang = st.selectbox("Exercise Induced Angina (1=Yes, 0=No)", options=[1, 0])
slope = st.selectbox("Slope of Peak Exercise ST Segment (0, 1, 2)", options=[0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-4)", options=[0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (1=Normal, 2=Fixed Defect, 3=Reversible Defect)", options=[1, 2, 3])

# Combine inputs into a single DataFrame
user_input = pd.DataFrame({
    'age': [age], 'sex': [sex], 'cp': [cp], 'trestbps': [trestbps],
    'chol': [chol], 'fbs': [fbs], 'restecg': [restecg], 'thalach': [thalach],
    'exang': [exang], 'slope': [slope], 'ca': [ca], 'thal': [thal]
})

# Predict using the model
if st.button("Predict"):
    if 'rf_model' in locals():
        try:
            prediction = rf_model.predict(user_input)
            if prediction[0] == 0:
                st.success("The patient is NOT likely to have heart disease.")
            else:
                st.warning("The patient is LIKELY to have heart disease.")
        except Exception as e:
            st.error(f"Error during prediction: {e}")
    else:
        st.error("Model is not loaded. Please resolve the issue.")






