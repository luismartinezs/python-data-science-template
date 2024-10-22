from .router import router
from .summarizer import summarizer
from .translator import translator
from .sentiment_analyzer import sentiment_analyzer

agents = {
    "router": router,
    "summarizer": summarizer,
    "translator": translator,
    "sentiment_analyzer": sentiment_analyzer,
}

__all__ = ["agents"]
