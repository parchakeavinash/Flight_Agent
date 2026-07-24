i want to build an AI Travel Booking system multi AGent system
along with we will use 4 specilzed AI agents:
- flight agent
- hotel agent
- itinerary agent
- final response Agent

Each aI agent performs its own task and together they work as one intelligent system


firist we will create an flight search tool using aviationstack api 

in that we will store th flight record
eg-
airline = 'emirates'
departure = 'Mumbai'
arrival = 'Mumbai international'
status = 'active'

✈ Emirates
📍 Mumbai → Dubai
🟢 Status: Active

                   User Query
                        │
                        ▼
               Parser Agent (LLM)
                        │
                        ▼
                 TravelDetails
                        │
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
 Flight Agent      Hotel Agent     Itinerary Agent
      │                 │                 │
      └─────────────────┴─────────────────┘
                        │
                        ▼
                  Final Response


User Query
      │
      ▼
Parser Agent
      │
      ▼
TravelDetails
      │
      ▼
Hotel Agent
      │
Build optimized search query
      │
      ▼
Tavily Tool
      │
Search the web
      │
      ▼
Hotel Results


my Parse agnet workflow

User Query
      │
      ▼
Parser Agent
      │
extract_travel_details()   ← Only 1 LLM call
      │
      ▼
TravelDetails
      │
 ┌────┴─────────┐
 ▼              ▼
Flight Agent   Hotel Agent
 ▼              ▼
Flight Tool    Hotel Tool
