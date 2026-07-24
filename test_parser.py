from app.services.travel_parser import extract_travel_details

query = """
I want to travel from Hyderabad to Dubai on 20 December with my wife.
My budget is ₹1,50,000.
Book a 4-star hotel near Burj Khalifa.
"""

travel = extract_travel_details(query)

print(travel)