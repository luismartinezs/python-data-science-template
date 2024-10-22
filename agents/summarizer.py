import ell
from ell import Message
from typing import List

ell.init(store="./logdir")


@ell.complex(model="gpt-4o-mini")
def summarizer(text: str) -> List[Message]:
    """You are a summarizer assistant. Summarize the given text concisely."""
    return [
        ell.user(f"Please provide a concise summary of the following text:\n\n{text}")
    ]


summarizer.description = "Summarizes the given text concisely."
summarizer.arguments = [
    {"name": "text", "type": "str", "description": "The text to be summarized"}
]
