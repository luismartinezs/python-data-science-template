import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from ell import Message
from agents.travel_planner_strout import (
    travel_planner_strout,
    TravelInfo,
    AgentResponse,
)


def main():
    collected_data = TravelInfo()

    print("Welcome to the Travel Planner Assistant!")
    print("You can start by telling me about your travel plans.")

    while True:
        # Get user input
        user_input = input("You: ").strip()
        if not user_input:
            print("Please enter some information to continue.")
            continue

        # Call the travel_planner agent with the collected data and latest user message
        agent_response_message: Message = travel_planner_strout(
            collected_data, user_input
        )

        # Parse the agent's JSON response into the AgentResponse model
        agent_response: AgentResponse = (
            agent_response_message.parsed
        )  # This should be an AgentResponse object

        # Print the agent's message
        print(f"Agent: {agent_response.message}")

        # If the conversation is complete, break the loop
        if agent_response.is_complete:
            break

        # Update the collected data based on the user's latest message
        # We'll use a simple keyword matching approach for the demo
        user_input_lower = user_input.lower()

        # Update destination
        if collected_data.destination is None:
            if "to" in user_input_lower or "destination" in user_input_lower:
                collected_data.destination = user_input

        # Update travel dates
        if collected_data.travel_dates is None:
            if (
                "from" in user_input_lower
                or "on" in user_input_lower
                or "dates" in user_input_lower
            ):
                collected_data.travel_dates = user_input

        # Update budget
        if collected_data.budget is None:
            if (
                "budget" in user_input_lower
                or "$" in user_input_lower
                or "dollars" in user_input_lower
            ):
                collected_data.budget = user_input

        # Update interests
        if collected_data.interests is None:
            if (
                "interested in" in user_input_lower
                or "like" in user_input_lower
                or "interests" in user_input_lower
            ):
                collected_data.interests = user_input

        # Alternatively, you could use NLP techniques or pattern matching to extract information more accurately

    # Print the final itinerary
    print("\nFinal Itinerary:")
    print(agent_response.message)


if __name__ == "__main__":
    main()
