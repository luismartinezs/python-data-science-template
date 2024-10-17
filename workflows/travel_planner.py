import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from ell import Message, ell
from typing import List
from agents.travel_planner import travel_planner


def main():
    # Initialize the conversation history
    conversation: List[Message] = []

    print("Welcome to the Travel Planner Assistant!")
    print("You can start by telling me about your travel plans.")

    while True:
        # Get user input
        user_input = input("You: ").strip()
        if not user_input:
            print("Please enter some information to continue.")
            continue

        conversation.append(ell.user(user_input))
        agent_response: Message = travel_planner(conversation)
        conversation.append(agent_response)
        print(f"Agent: {agent_response.text}")
        if agent_response.text.strip().startswith("ITINERARY:"):
            break

    print("\nFinal Itinerary:")
    print(agent_response.text)


if __name__ == "__main__":
    main()
