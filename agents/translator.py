from ell import ell
from ell import Message
from typing import List

ell.init(store="./logdir")


@ell.complex(model="gpt-4o-mini")
def translator(text: str) -> List[Message]:
    """You are a translator assistant. Translate the given text to the target language specified."""
    return [ell.user(text)]


translator.description = "Translates the given text to the specified target language."
translator.arguments = [
    {"name": "text", "type": "str", "description": "The text to be translated"},
]
