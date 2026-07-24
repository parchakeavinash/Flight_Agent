from langchain_core.messages import HumanMessage, SystemMessage
from app.schemas.flight_schema import FlightSearchRequest
from config import settings
from langchain_groq import ChatGroq

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key=settings.GROQ_API_KEY,
)


structured_llm = llm.with_structured_output(FlightSearchRequest)


def extract_flight_info(user_query: str) -> FlightSearchRequest:

    response = structured_llm.invoke(
        [
            SystemMessage(
                content="""
You are an expert travel assistant.

Extract ONLY the following information:

- departure_city
- destination_city
- departure_date

If any field is missing, return an empty string.
"""
            ),
            HumanMessage(content=user_query),
        ]
    )

    return response