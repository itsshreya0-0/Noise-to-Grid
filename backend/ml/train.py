import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("../../data/sample_noise_data.csv")
df["peak"] = (df["db_level"] > 80).astype(int)

X = df[["db_level", "piezo_voltage"]]
y = df["peak"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained.")
