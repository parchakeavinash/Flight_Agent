from app.utils.airport_codes import AIRPORT_CODES

def get_airport_code(city: str):

    return AIRPORT_CODES.get(city)