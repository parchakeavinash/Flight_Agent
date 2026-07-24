import os
import operator
from langchain_core.prompts import prompt
import psycopg
import json

from typing import TypedDict, Annotated,List
from langgraph.graph import StateGraph, START, END
# from langgraph.checkpoint.postgres import PostgresSaver
from langchain_core.messages import(
    AnyMessage,
    HumanMessage,
    AIMessage,
    SystemMessage
)
from langchain_groq import ChatGroq

from app.tools.tavily_tool import tavily_search
from app.tools.flight_tool import flight_search

from config import api_key

llm = ChatGroq(
    model = "llama-3.3-70b-versatile"
)

# State
class TravelState(TypedDict):
    messages: Annotated[List[AnyMessage],operator.add]
    user_query: str
    flight_result: str
    hotel_result: str
    itinerary: str
    llm_calls: int

#create agents

# flight agent

def flight_agent(state: TravelState):
    query = state['user_query']
    flight_data = flight_search(query)
    return{
        "flight_result": flight_data,
        "messages":[
            AIMessage(content = f'Flight result fetched')
        ],
        "llm_calls": state.get('llm_calls',0) +1
    }

# hostel agent

def hotel_agent(state: TravelState):
    query = state['user_query']
    hostel_data = tavily_search(query)

    return{
        'hotel_result': hostel_data,
        'messages': [
            AIMessage(content=f'Hotel information fetched..')
        ],
        'llm_calls': state.get('llm_calls',0)+1
    }


# itinerary agent
def itinerary_agent(state: TravelState):
    prompt = f"""
    User Query:
    {state["user_query"]}

    Flights:
    {json.dumps(state["flight_result"], indent=2)}

    Hotels:
    {json.dumps(state["hotel_result"], indent=2)}

    Create a personalized travel itinerary based on the information.
    Generate:
    1. A day-wise travel itinerary.
    2. Recommended sightseeing places.
    3. Local transportation suggestions.
    4. Food recommendations.
    5. Estimated travel tips.

"""

    response = llm.invoke([
        SystemMessage(
            content='You are an expert travel planner who creates detailed, practical, and personalized travel itineraries'
        ),
        HumanMessage(content=prompt),
   ])

    return{
    'planner':response.content,
    'messages':[response],
    'llm_calls':state.get('llm_calls',0)+1,

   }

#final response agent
def final_agenet(state:TravelState):
    final_prompt = f"""
    Generate the final travel plan for the user.

    Flight Details:
    {state["flight_results"]}

    Hotel Details:
    {state["hotel_results"]}

    Travel Itinerary:
    {state["itinerary"]}

    Present the response in a clean and user-friendly format.
"""

    response = llm.invoke([
        SystemMessage(content = 'You are an expert travel assistant.'),
        HumanMessage(content =final_prompt)
    ])

    return {
        'messages':[response],
        'llm_calls': state.get('llm_calls',0) + 1
    }

# build graph
graph = StateGraph(TravelState)

graph.add_node('flight_agent',flight_agent)
graph.add_node('hotel_agent',hotel_agent)
graph.add_node('itinerary_agent',itinerary_agent)
graph.add_node('final_agent',final_agenet)

graph.add_edge(START, 'flight_agent')
graph.add_edge('flight_agent', 'hotel_agent')
graph.add_edge("hotel_agent", 'itinerary_agent')
graph.add_edge("itinerary_agent", 'final_agent')
graph.add_edge("final_agent", END)

app = graph.compile()

if __name__== '__main__':
    user_query = input("Enter you travel request")

    result = app.invoke(
        {
            "messages":[HumanMessage(content=user_query)],
            "user_query": user_query,
            "flight_results": [],
            "hotel_results": [],
            "itinerary": "",
            "llm_calls": 0,

        }
    )

    print("\n========== FINAL RESPONSE ==========\n")

    for msg in result['messages']:
        print(msg.content)
