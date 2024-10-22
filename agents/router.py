from ell import ell
from ell import Message
from pydantic import BaseModel, Field
from typing import Any, Dict, Optional, Callable

ell.init(store="./logdir")


class RouterResponse(BaseModel):
    agent_name: str = Field(description="The name of the selected agent")


@ell.complex(model="gpt-4o-mini", response_format=RouterResponse)
def router(
    user_query: str,
    agents_config: Dict[str, Dict[str, Any]],
) -> RouterResponse:
    agent_descriptions = "\n".join(
        [f"- {name}: {info['description']}" for name, info in agents_config.items()]
    )

    system_message = f"""You are a routing assistant. Your task is to determine which agent is best suited to handle the user's query.

The available agents are:
{agent_descriptions}

Your response should be the agent name.
If none of the agents are suitable, respond with "{{"agent_name": "None"}}."
"""
    prompt = f"""User query: "{user_query}"

Which agent should handle this request? Provide the agent name and any necessary arguments."""

    return [
        ell.system(system_message),
        ell.user(prompt),
    ]


router.description = "Determines which agent is best suited to handle the user's query."
router.arguments = [
    {"name": "query", "type": "str", "description": "The user's query"},
    {"name": "agents", "type": "Dict[str, str]", "description": "The available agents"},
]
