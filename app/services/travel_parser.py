from langchain_core.messages import HumanMessage, SystemMessage
from config import settings
from app.schemas.travel_schema import TravelDetails
from langchain_groq import ChatGroq


llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key=settings.GROQ_API_KEY,
)

structured_llm = llm.with_structured_output(TravelDetails)

def extract_travel_details(user_query: str) -> TravelDetails:

    response = structured_llm.invoke(
        [
            SystemMessage(
                content="""
You are an expert travel planner.

Extract the following fields.

- departure_city
- destination_city
- departure_date
- return_date
- travelers
- budget
- hotel_type
- location_preference

If a field is not mentioned,
return an empty string or null.
"""
            ),
            HumanMessage(content=user_query),
        ]
    )

    return response