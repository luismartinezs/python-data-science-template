from .router import router
from .summarizer import summarizer
from .translator import translator
from .sentiment_analyzer import sentiment_analyzer
from .travel_planner_strout import travel_planner_strout
from .travel_planner import travel_planner
from .latent_space_activation import latent_space_activation

agents = {
    "router": router,
    "summarizer": summarizer,
    "translator": translator,
    "sentiment_analyzer": sentiment_analyzer,
    "travel_planner_strout": travel_planner_strout,
    "travel_planner": travel_planner,
    "latent_space_activation": latent_space_activation,
}

__all__ = ["agents"]
