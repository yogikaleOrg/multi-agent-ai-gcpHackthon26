from fastapi import FastAPI
from app.agents.orchestrator import Orchestrator

app = FastAPI(title="Multi-Agent AI System")

orch = Orchestrator()

@app.post("/execute")
def execute(req: dict):
    return orch.handle(req)

@app.get("/")
def root():
    return {"message": "Multi-Agent AI System Running"}