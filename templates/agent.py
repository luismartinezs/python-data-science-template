import ell
from ell import Message
from typing import List

ell.init(store="./logdir")


class Agent:
    def __init__(self, description):
        self.description = description

    @ell.complex(model="gpt-4o-mini")
    def query_llm(self, input_param: str) -> List[Message]:
        """You are an [AGENT_TYPE] assistant. [AGENT_DESCRIPTION]"""
        return [ell.user(f"You are a helpful assistant\n\n{input_param}")]
