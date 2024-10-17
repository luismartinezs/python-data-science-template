import ell
from ell import Message
from typing import List

ell.init(store="./logdir")


@ell.complex(model="gpt-4o-mini")
def agent_name(input_param: str) -> List[Message]:
    """You are an [AGENT_TYPE] assistant. [AGENT_DESCRIPTION]"""
    return [ell.user(f"[AGENT_PROMPT]\n\n{input_param}")]


agent_name.description = "[AGENT_DESCRIPTION]"
agent_name.arguments = [
    {"name": "input_param", "type": "str", "description": "[PARAMETER_DESCRIPTION]"}
]
