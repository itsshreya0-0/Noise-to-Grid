import streamlit as st
import requests

st.title("Noise-to-Grid Dashboard")

db = st.slider("Noise Level (dB)", 40, 120, 70)
piezo = st.slider("Piezo Voltage", 0.0, 5.0, 1.0)

if st.button("Predict Peak"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"db_level": db, "piezo_voltage": piezo}
    )
    st.write(response.json())
