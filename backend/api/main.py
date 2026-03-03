from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import joblib
import pandas as pd

app = FastAPI()

# ---- FIXED MODEL PATH ----
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "ml" / "model.pkl"
model = joblib.load(MODEL_PATH)
# --------------------------

class SensorData(BaseModel):
    db_level: float
    piezo_voltage: float

@app.get("/")
def root():
    return {"message": "Noise-to-Grid API running"}

@app.post("/predict")
def predict(data: SensorData):
    df = pd.DataFrame(
        [[data.db_level, data.piezo_voltage]],
        columns=["db_level", "piezo_voltage"]
    )

    prediction = model.predict(df)[0]
    return {"predicted_peak": int(prediction)})}
