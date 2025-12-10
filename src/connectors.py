import os
import requests

class ConnectorResult:
    def __init__(self, provider: str, ok: bool, status_code: int = 0, message: str = ""):
        self.provider = provider
        self.ok = ok
        self.status_code = status_code
        self.message = message

    def to_dict(self):
        return {
            "provider": self.provider,
            "ok": self.ok,
            "status_code": self.status_code,
            "message": self.message,
        }

# Note: Most provider endpoints require auth + approved accounts. We provide
# simple "ping" style requests where feasible, else we simulate key presence.

HEADERS_JSON = {"Accept": "application/json"}

def _safe_get(url, headers=None, params=None):
    try:
        r = requests.get(url, headers=headers or HEADERS_JSON, params=params, timeout=8)
        return ConnectorResult("GET", r.ok, r.status_code, r.text[:200])
    except Exception as e:
        return ConnectorResult("GET", False, 0, str(e))

# Amadeus (example: check if key is set; real token flow requires OAuth)
AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY", "")
AMBOSEC = os.getenv("AMADEUS_API_SECRET", "")

def test_amadeus():
    if not AMADEUS_API_KEY or not AMBOSEC:
        return ConnectorResult("amadeus", False, 0, "Missing AMADEUS_API_KEY/SECRET")
    # Public metadata (placeholder; actual API needs OAuth token)
    return ConnectorResult("amadeus", True, 200, "Keys present (OAuth required for real calls)")

# Skyscanner (via RapidAPI commonly)
SKYSCANNER_API_KEY = os.getenv("SKYSCANNER_API_KEY", "")

def test_skyscanner():
    if not SKYSCANNER_API_KEY:
        return ConnectorResult("skyscanner", False, 0, "Missing SKYSCANNER_API_KEY")
    # Example endpoint via RapidAPI often requires specific host header; simulate presence
    return ConnectorResult("skyscanner", True, 200, "Key present (endpoint requires RapidAPI host)")

# Yelp Fusion
YELP_API_KEY = os.getenv("YELP_API_KEY", "")

def test_yelp():
    if not YELP_API_KEY:
        return ConnectorResult("yelp", False, 0, "Missing YELP_API_KEY")
    headers = {"Authorization": f"Bearer {YELP_API_KEY}", **HEADERS_JSON}
    # Simple search ping to a known location
    url = "https://api.yelp.com/v3/businesses/search"
    result = _safe_get(url, headers=headers, params={"location": "Paris", "limit": 1})
    result.provider = "yelp"
    return result

# Google Places
GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY", "")

def test_google_places():
    if not GOOGLE_PLACES_API_KEY:
        return ConnectorResult("google_places", False, 0, "Missing GOOGLE_PLACES_API_KEY")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {"query": "museum in London", "key": GOOGLE_PLACES_API_KEY}
    result = _safe_get(url, params=params)
    result.provider = "google_places"
    return result
