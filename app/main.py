from flask import Flask, jsonify, request

app = Flask(__name__)

ENGINE = {"rpm": 0, "coolant_temp": 70.0, "oil_pressure": 2.0, "status": "idle"}
WAYPOINTS = [
    {"id": 1, "name": "Port Tulcea", "lat": 45.186, "lon": 28.805},
    {"id": 2, "name": "Canal Sulina (mm10)", "lat": 45.158, "lon": 29.659},
]

@app.get("/health")
def health():
    return {"status": "ok"}, 200

@app.get("/engine")
def get_engine():
    return jsonify(ENGINE)

@app.post("/engine")
def update_engine():
    data = request.get_json() or {}
    for k in ("rpm", "coolant_temp", "oil_pressure", "status"):
        if k in data:
            ENGINE[k] = data[k]
    return jsonify(ENGINE), 200

@app.get("/waypoints")
def list_waypoints():
    return jsonify(WAYPOINTS)

@app.post("/waypoints")
def add_waypoint():
    data = request.get_json() or {}
    if not all(k in data for k in ("name", "lat", "lon")):
        return {"error": "name, lat, lon required"}, 400
    new_id = max([w["id"] for w in WAYPOINTS] or [0]) + 1
    wp = {"id": new_id, "name": data["name"], "lat": float(data["lat"]), "lon": float(data["lon"])}
    WAYPOINTS.append(wp)
    return wp, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
