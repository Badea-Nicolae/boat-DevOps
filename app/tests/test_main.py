import requests

def test_health_endpoint():
    resp = requests.get("http://localhost:8000/health", timeout=5)
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
