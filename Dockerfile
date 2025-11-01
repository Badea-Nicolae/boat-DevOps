from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, List
import uuid

app = FastAPI(title="Boat DevOps API", version="1.0.0")

# --- MODELE ---
class EngineData(BaseModel):
    rpm: int = Field(..., ge=0)
    coolant_temp: float = Field(..., ge=-50, le=150)
    oil_pressure: float = Field(..., ge=0)

class WaypointIn(BaseModel):
    name: str
    lat: float
    lon: float

class Waypoint(WaypointIn):
    id: str

# --- STATE IN-MEMORY ---
engine_state: Dict[str, float | int] = {
    "rpm": 0,
    "coolant_temp": 70.0,
    "oil_pressure": 2.5,
}
waypoints: Dict[str, Waypoint] = {}

# --- ENDPOINTS ---
@app.get("/api/v1/health")
def health():
    return {"status": "ok"}

@app.get("/api/v1/engine")
def get_engine():
    return engine_state

@app.post("/api/v1/engine", status_code=201)
def update_engine(data: EngineData):
    engine_state.update(data.model_dump())
    return engine_state

@app.get("/api/v1/waypoints", response_model=List[Waypoint])
def list_waypoints():
    return list(waypoints.values())

@app.post("/api/v1/waypoints", response_model=Waypoint, status_code=201)
def add_waypoint(item: WaypointIn):
    wid = str(uuid.uuid4())[:8]
    wp = Waypoint(id=wid, **item.model_dump())
    waypoints[wid] = wp
    return wp

@app.delete("/api/v1/waypoints/{wid}", status_code=204)
def delete_waypoint(wid: str):
    if wid not in waypoints:
        raise HTTPException(status_code=404, detail="Waypoint not found")
    del waypoints[wid]
