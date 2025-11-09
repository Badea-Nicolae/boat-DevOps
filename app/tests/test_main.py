from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/api/v1/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_get_engine():
    r = client.get("/api/v1/engine")
    assert r.status_code == 200
    data = r.json()
    assert "rpm" in data
    assert "temp_c" in data
    assert "oil_kpa" in data

def test_update_engine():
    test_data = {"rpm": 2500, "temp_c": 85.5, "oil_kpa": 350.0}
    r = client.post("/api/v1/engine", json=test_data)
    assert r.status_code == 201
    assert r.json() == test_data

def test_waypoints():
    # Test adding a waypoint
    test_waypoint = {"name": "Test Point", "lat": 45.0, "lon": 25.0}
    r = client.post("/api/v1/waypoints", json=test_waypoint)
    assert r.status_code == 201
    data = r.json()
    assert "id" in data
    wid = data["id"]
    
    # Test listing waypoints
    r = client.get("/api/v1/waypoints")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    
    # Test deleting waypoint
    r = client.delete(f"/api/v1/waypoints/{wid}")
    assert r.status_code == 204
