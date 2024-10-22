# travel_planner.py

import ell
from ell import Message
from typing import List

# Initialize the ell-ai library
ell.init(store="./logdir")  # Adjust the store path as needed


# Define the TravelPlanner agent
@ell.complex(model="gpt-4o-mini")
def travel_planner(conversation_history: List[Message]) -> List[Message]:
    """
    You are a travel planning assistant.

    **Instructions:**
    - Gather the following required information from the user:
      - **Destination**
      - **Travel dates**
      - **Budget**
      - **Interests** (e.g., culture, adventure, relaxation)
    - Review the conversation history to determine which information has been provided.
    - If any required information is missing, ask the user for the missing details.
    - Once all required information is collected, provide a detailed travel itinerary based on the user's preferences.
    - When providing the itinerary, begin your response with "**ITINERARY:**" to indicate completion.
    - Do not mention the information already collected; focus on what's missing.
    """

    # The agent combines the system prompt with the conversation history
    return [
        ell.system(
            "You are a helpful travel planning assistant who collects required information and provides an itinerary."
        ),
        *conversation_history,
    ]


# Optionally, you can add a description and arguments for use with the router agent
travel_planner.description = "Interacts with the user to plan a travel itinerary by collecting necessary information."
travel_planner.arguments = [
    {
        "name": "conversation_history",
        "type": "List[Message]",
        "description": "The conversation history with the user",
    },
]
