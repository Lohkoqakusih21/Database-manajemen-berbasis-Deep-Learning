import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    df = pd.DataFrame({"value": data})
    model = IsolationForest(contamination=0.1)
    df["anomaly"] = model.fit_predict(df[["value"]])
    anomalies = df[df["anomaly"] == -1]["value"].tolist()
    return anomalies
