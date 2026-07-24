import requests
from config import api_key

def flight_search(query) ->str:
    url  = "https://api.aviationstack.com/v1/flights"

    params = {
        'access_key': api_key.AVIATIONSTACK_API_KEY,
        'limit': 5
    }

    response = requests.get(url,params=params)
    response.raise_for_status()

    flights = response.json()['data']

    saved_flight = []

    for flight in flights:
        airline = flight.get("airline", {}).get("name", "Unknown")
        departure = flight.get("departure", {}).get("airport", "Unknown")
        arrival = flight.get("arrival", {}).get("airport", "Unknown")
        status = flight.get("flight_status", "Unknown")

    saved_flight.append({
        "airline": airline,
        "departure": departure,
        "arrival": arrival,
        "status": status,
    })

    return saved_flight

   