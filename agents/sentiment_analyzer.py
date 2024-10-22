from ell import ell
from ell import Message
from typing import List

ell.init(store="./logdir")


@ell.complex(model="gpt-4o-mini")
def sentiment_analyzer(text: str) -> List[Message]:
    """You are a sentiment analysis assistant. Analyze the sentiment of the given text and provide a brief explanation."""
    return [
        ell.user(
            f"Analyze the sentiment of the following text and explain your reasoning:\n\n{text}"
        )
    ]


sentiment_analyzer.description = "Analyzes the sentiment of given text and provides a brief explanation of the analysis."
sentiment_analyzer.arguments = [
    {"name": "text", "type": "str", "description": "The text to be analyzed"},
]
