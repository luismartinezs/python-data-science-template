import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.latent_space_activation import latent_space_activation

latent_space_activation(
    "Who is the single most important person in the entire history of Ancient Rome?",
    "Ancient Rome",
)
