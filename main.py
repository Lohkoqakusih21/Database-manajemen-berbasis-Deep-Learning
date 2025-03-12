from fastapi import FastAPI
from backend.query_generator import generate_sql_query
from backend.query_optimizer import optimize_query
from backend.anomaly_detector import detect_anomalies

app = FastAPI()

@app.post("/generate_query")
def generate_query(request: dict):
    return {"sql": generate_sql_query(request["query"], request["schema"])}

@app.post("/optimize_query")
def optimize(request: dict):
    return {"recommendations": optimize_query(request["query"])}

@app.post("/detect_anomalies")
def detect(request: dict):
    return {"anomalies": detect_anomalies(request["data"])}
