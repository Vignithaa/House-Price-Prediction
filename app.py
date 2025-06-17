import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model/linear_model.pkl', 'rb'))

st.title("🏠 Boston House Price Predictor")

CRIM = st.number_input("Crime Rate", 0.0, 100.0)
RM = st.number_input("Average Number of Rooms", 1.0, 10.0)
AGE = st.number_input("Proportion of Older Homes (%)", 0.0, 100.0)
TAX = st.number_input("Property Tax Rate", 0.0, 800.0)

if st.button("Predict Price"):
    input_data = np.array([[CRIM, 0, 0, 0, 0, RM, 0, AGE, 0, 0, TAX, 0, 0]])
    prediction = model.predict(input_data)
    st.success(f"Predicted House Price: ${prediction[0]*1000:.2f}")
