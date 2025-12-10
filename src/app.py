from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import json
import mysql.connector
from src.connectors import test_amadeus, test_skyscanner, test_yelp, test_google_places
from src.connectors_extra import test_tripadvisor, test_rail_europe, test_uber, test_here, test_overpass
from src.connectors_more import test_deutsche_bahn, test_foursquare, test_opentable

app = Flask(__name__, static_folder="../public", static_url_path="")
CORS(app)

# Load curated examples
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'curated_examples.json')
with open(DATA_PATH, 'r', encoding='utf-8') as f:
    CURATED = json.load(f)

# MySQL connection
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'db'),
    'user': os.getenv('DB_USER', 'travel'),
    'password': os.getenv('DB_PASSWORD', 'travelpwd'),
    'database': os.getenv('DB_NAME', 'travel_ai')
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.get('/api/curated/<region>')
def get_curated(region):
    data = CURATED.get(region)
    if not data:
        return jsonify({"error": "Region not found"}), 404
    return jsonify(data)

@app.post('/api/selections')
def save_selections():
    payload = request.json or {}
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO selections (region, transport, accommodation, food, sites, onsite_transport)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            payload.get('region'),
            payload.get('transport'),
            json.dumps(payload.get('accommodation')),
            json.dumps(payload.get('food')),
            json.dumps(payload.get('sites')),
            payload.get('onsite_transport')
        )
    )
    conn.commit()
    cur.close(); conn.close()
    return jsonify({"status": "saved"})

@app.get('/api/selections')
def list_selections():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, region, transport, accommodation, food, sites, onsite_transport, created_at FROM selections ORDER BY id DESC LIMIT 50")
    rows = cur.fetchall()
    cur.close(); conn.close()
    return jsonify(rows)

# Simple health checks
@app.get('/api/health')
def health():
    return jsonify({"ok": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

# Test routes
@app.get('/api/test/amadeus')
def api_test_amadeus():
    return jsonify(test_amadeus().to_dict())

@app.get('/api/test/skyscanner')
def api_test_skyscanner():
    return jsonify(test_skyscanner().to_dict())

@app.get('/api/test/yelp')
def api_test_yelp():
    return jsonify(test_yelp().to_dict())

@app.get('/api/test/google_places')
def api_test_google_places():
    return jsonify(test_google_places().to_dict())

@app.get('/api/test/tripadvisor')
def api_test_tripadvisor():
    return jsonify(test_tripadvisor().to_dict())

@app.get('/api/test/rail_europe')
def api_test_rail_europe():
    return jsonify(test_rail_europe().to_dict())

@app.get('/api/test/uber')
def api_test_uber():
    return jsonify(test_uber().to_dict())

@app.get('/api/test/here')
def api_test_here():
    return jsonify(test_here().to_dict())

@app.get('/api/test/overpass')
def api_test_overpass():
    return jsonify(test_overpass().to_dict())

@app.get('/api/test/deutsche_bahn')
def api_test_db():
    return jsonify(test_deutsche_bahn().to_dict())

@app.get('/api/test/foursquare')
def api_test_foursquare():
    return jsonify(test_foursquare().to_dict())

@app.get('/api/test/opentable')
def api_test_opentable():
    return jsonify(test_opentable().to_dict())
