import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import pydeck as pdk

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Noise-to-Grid Dashboard", layout="wide")

st.title("Noise-to-Grid Smart City Dashboard")
st.markdown("AI-powered urban noise energy harvesting system")

# -----------------------------
# Sidebar Controls
# -----------------------------
st.sidebar.header("Sensor Input")

db = st.sidebar.slider("Noise Level (dB)", 40, 120, 70)
piezo = st.sidebar.slider("Piezo Voltage (V)", 0.0, 5.0, 1.0)

# -----------------------------
# Metrics Layout
# -----------------------------
col1, col2 = st.columns(2)

col1.metric("Current Noise Level", f"{db} dB")
col2.metric("Piezo Voltage", f"{piezo} V")

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict Peak"):

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"db_level": db, "piezo_voltage": piezo}
    )

    prediction = response.json()["predicted_peak"]

    # Prediction Output
    if prediction == 1:
        st.success("Peak Noise Detected – Harvest Mode Activated")
    else:
        st.warning("Normal Noise Level – Harvest Mode Idle")

    # -----------------------------
    # Energy Conversion Logic
    # -----------------------------
    if prediction == 1:
        energy_generated = piezo * 0.08
    else:
        energy_generated = 0

    st.metric("Estimated Energy Generated (Wh)", round(energy_generated, 3))

    # -----------------------------
    # Noise History Graph
    # -----------------------------
    st.subheader("Noise Trend")

    noise_history = [60, 65, 70, 75, 80, db]

    df = pd.DataFrame({
        "Time": ["T1","T2","T3","T4","T5","Now"],
        "Noise (dB)": noise_history
    })

    fig, ax = plt.subplots()

    ax.plot(df["Time"], df["Noise (dB)"], marker="o")

    ax.set_xlabel("Time")
    ax.set_ylabel("Noise Level (dB)")
    ax.set_title("Noise Level Trend")

    st.pyplot(fig)

    # -----------------------------
    # Energy Bar Graph
    # -----------------------------
    st.subheader("Energy Generated")

    energy_data = {
        "Source": ["Piezo Panel"],
        "Energy (Wh)": [energy_generated]
    }

    df_energy = pd.DataFrame(energy_data)

    fig2, ax2 = plt.subplots()

    ax2.bar(df_energy["Source"], df_energy["Energy (Wh)"])

    ax2.set_ylabel("Energy (Wh)")
    ax2.set_title("Harvested Energy")

    st.pyplot(fig2)

# -----------------------------
# City Noise Map
# -----------------------------


st.subheader("Urban Noise Monitoring Map")

map_data = pd.DataFrame({
    "lat": [11.0168, 11.018, 11.0155],
    "lon": [76.9558, 76.958, 76.953],
    "noise": [60, 85, db]
})

# Color logic
def get_color(noise):
    if noise > 80:
        return [255, 0, 0]      # Red → High noise
    elif noise > 65:
        return [255, 165, 0]    # Orange → Medium noise
    else:
        return [0, 200, 0]      # Green → Low noise

map_data["color"] = map_data["noise"].apply(get_color)

layer = pdk.Layer(
    "ScatterplotLayer",
    map_data,
    get_position='[lon, lat]',
    get_fill_color='color',
    get_radius=120,
)

view_state = pdk.ViewState(
    latitude=11.0168,
    longitude=76.9558,
    zoom=13,
    pitch=0
)

st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state
))
