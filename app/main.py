# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, List
import uuid

app = FastAPI(title="Boat DevOps API", version="1.0.0")

# --- MODELE ---
class EngineData(BaseModel):
    rpm: int = Field(ge=0, le=6000)
    temp_c: float = Field(ge=-40, le=150)
    oil_kpa: float = Field(ge=0, le=1000)

class Waypoint(BaseModel):
    id: str | None = None
    name: str
    lat: float = Field(ge=-90, le=90)
    lon: float = Field(ge=-180, le=180)

# --- STARE IN-MEMORY ---
engine_state: Dict[str, float | int] = {"rpm": 0, "temp_c": 20.0, "oil_kpa": 0.0}
waypoints: Dict[str, Waypoint] = {}

# --- HEALTH ---
@app.get("/api/v1/health")
def health():
    return {"status": "ok"}

# --- ENGINE ---
@app.get("/api/v1/engine", response_model=EngineData)
def get_engine():
    return EngineData(**engine_state)

@app.post("/api/v1/engine", response_model=EngineData, status_code=201)
def update_engine(data: EngineData):
    engine_state.update(data.model_dump())
    return EngineData(**engine_state)

# --- WAYPOINTS ---
@app.get("/api/v1/waypoints", response_model=List[Waypoint])
def list_waypoints():
    return list(waypoints.values())

@app.post("/api/v1/waypoints", response_model=Waypoint, status_code=201)
def add_waypoint(item: Waypoint):
    wid = (uuid.uuid4().hex)[:8]
    item.id = wid
    waypoints[wid] = item
    return item

@app.delete("/api/v1/waypoints/{wid}", status_code=204)
def delete_waypoint(wid: str):
    if wid not in waypoints:
        raise HTTPException(status_code=404, detail="Waypoint not found")
    waypoints.pop(wid)
