# Travel API Providers (10 per Section)

Note: Many providers require manual signup and API key approval. Automatic key requests are not possible purely from code without user authorization. Below are sources to consider; use environment variables to store issued keys.

## Transport from Home (Bus/Train/Airplane)

- Amadeus APIs (flights)
- Skyscanner Flights API
- Kiwi.com Tequila API
- Lufthansa Open API
- British Airways API (limited)
- Rail Europe API (partner access)
- Deutsche Bahn API
- TransportAPI (UK)
- Rome2Rio API (commercial)
- FlixBus API (partner)

## Accommodation

- Booking.com API (partner)
- Expedia Rapid API
- Hotels.com API (via Expedia Group)
- Airbnb Partner API (limited access)
- Agoda Affiliate API
- TripAdvisor Content API
- Hotelbeds API
- Amadeus Hotel API
- Priceline Partner API
- RapidAPI aggregations (various hotel endpoints)

## Food / Restaurants

- Yelp Fusion API
- Google Places API
- Zomato / Zomato v2 APIs (availability varies)
- TripAdvisor Restaurants API
- OpenTable API (partner)
- FourSquare Places API
- Michelin Guide data (limited/partners)
- HappyCow API (vegetarian/vegan)
- RapidAPI food/restaurant aggregations
- RestApp/Restaurant APIs (various local data)

## Tourist & Cultural Sites

- Google Places (points of interest)
- TripAdvisor Attractions API
- FourSquare Places
- Wikidata/Wikipedia APIs
- OpenStreetMap Overpass API
- Cultural Heritage APIs (country specific)
- Museums APIs (country/city specific)
- UNESCO World Heritage API (third-party mirrors)
- City tourism boards APIs
- RapidAPI travel attractions endpoints

## On-site Transport

- Uber API
- Lyft API
- Bolt API
- FreeNow API
- Grab API (Asia)
- Ola API (India)
- City Public Transit GTFS/RT feeds
- Google Directions API
- Moovit API (partner)
- HERE Transit API

## Key Management

- Store keys in environment variables: `AMadeus_API_KEY`, `SKYSCANNER_API_KEY`, etc.
- Do not hard-code keys; use `.env` in dev and secrets in deployment.
- Some providers need business agreements; expect onboarding steps.
