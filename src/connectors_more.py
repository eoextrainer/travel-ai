import os
from src.connectors import ConnectorResult, _safe_get, HEADERS_JSON

# Deutsche Bahn (DB) - public timetable info often via open data; real API requires partner
DB_API_KEY = os.getenv("DB_API_KEY", "")

def test_deutsche_bahn():
    if not DB_API_KEY:
        return ConnectorResult("deutsche_bahn", False, 0, "Missing DB_API_KEY")
    return ConnectorResult("deutsche_bahn", True, 200, "Key present (partner API required)")

# Foursquare Places
FOURSQUARE_API_KEY = os.getenv("FOURSQUARE_API_KEY", "")

def test_foursquare():
    if not FOURSQUARE_API_KEY:
        return ConnectorResult("foursquare", False, 0, "Missing FOURSQUARE_API_KEY")
    url = "https://api.foursquare.com/v3/places/search"
    headers = {"Authorization": FOURSQUARE_API_KEY, **HEADERS_JSON}
    result = _safe_get(url, headers=headers, params={"near": "Paris", "limit": 1})
    result.provider = "foursquare"
    return result

# OpenTable (partner access)
OPENTABLE_API_KEY = os.getenv("OPENTABLE_API_KEY", "")

def test_opentable():
    if not OPENTABLE_API_KEY:
        return ConnectorResult("opentable", False, 0, "Missing OPENTABLE_API_KEY")
    return ConnectorResult("opentable", True, 200, "Key present (partner API required)")
