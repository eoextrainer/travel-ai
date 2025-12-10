import os
from src.connectors import ConnectorResult, _safe_get, HEADERS_JSON

# Additional providers: TripAdvisor, Rail Europe, Uber, HERE, OpenStreetMap Overpass

TRIPADVISOR_API_KEY = os.getenv("TRIPADVISOR_API_KEY", "")

def test_tripadvisor():
    if not TRIPADVISOR_API_KEY:
        return ConnectorResult("tripadvisor", False, 0, "Missing TRIPADVISOR_API_KEY")
    # Placeholder: Real endpoints require partner access
    return ConnectorResult("tripadvisor", True, 200, "Key present (partner API required)")

RAIL_EUROPE_API_KEY = os.getenv("RAIL_EUROPE_API_KEY", "")

def test_rail_europe():
    if not RAIL_EUROPE_API_KEY:
        return ConnectorResult("rail_europe", False, 0, "Missing RAIL_EUROPE_API_KEY")
    return ConnectorResult("rail_europe", True, 200, "Key present (partner API required)")

UBER_SERVER_TOKEN = os.getenv("UBER_SERVER_TOKEN", "")

def test_uber():
    if not UBER_SERVER_TOKEN:
        return ConnectorResult("uber", False, 0, "Missing UBER_SERVER_TOKEN")
    # Legacy endpoints deprecated; simulate key presence
    return ConnectorResult("uber", True, 200, "Key present (OAuth/partner required)")

HERE_API_KEY = os.getenv("HERE_API_KEY", "")

def test_here():
    if not HERE_API_KEY:
        return ConnectorResult("here", False, 0, "Missing HERE_API_KEY")
    url = "https://router.hereapi.com/v8/routes"
    params = {"transportMode": "car", "origin": "52.5,13.4", "destination": "52.52,13.45", "return": "summary", "apikey": HERE_API_KEY}
    result = _safe_get(url, params=params)
    result.provider = "here"
    return result

# OpenStreetMap Overpass (no key)

def test_overpass():
    url = "https://overpass-api.de/api/interpreter"
    # Simple query: fetch museums in Berlin area (very light)
    q = "[out:json];node[amenity=museum](52.49,13.35,52.55,13.45);out 1;"
    result = _safe_get(url, params={"data": q})
    result.provider = "overpass"
    return result
