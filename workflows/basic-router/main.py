import sys
from pathlib import Path

# Add the parent directory of 'workflows' to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from typing import Dict, Any
from ell import Message
from agents import agents, router

agents_config: Dict[str, Dict[str, Any]] = {
    agent_name.capitalize(): {"description": agent_func.description}
    for agent_name, agent_func in agents.items()
    if agent_name != "router"
}


def main() -> None:
    user_query = "Can you analyze the sentiment of this tweet: 'I absolutely love the new features in the latest software update! It's made my workflow so much smoother and efficient. #TechJoy'"

    # Use the router to determine the appropriate agent
    routing_response_message = router(user_query, agents_config)
    routing_response = routing_response_message.parsed
    print(routing_response)
    agent_name = routing_response.agent_name
    print(f"Router selected agent: {agent_name}")

    if agent_name in agents_config:
        # Get the agent function directly from the imported modules
        agent = agents[agent_name.lower()]

        # Call the agent with the entire user query
        response: Message = agent(user_query)

        print(f"\n{agent_name} Response:")
        print(response.text)
    else:
        print("\nI cannot assist with that request.")


if __name__ == "__main__":
    main()
