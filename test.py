from pydantic import BaseModel, Field
from typing import List
import random
class Strategy(BaseModel):
    description: str = Field(
        description="A brief one or two sentence description of the strategy"
    )

class StrategiesList(BaseModel):
    strategies: List[Strategy] = Field(
        description="A list of strategies to solve the problem"
    )


strategies = StrategiesList(strategies=[
    Strategy(description="Implement the Pomodoro Technique where you work for 25 minutes followed by a 5-minute break to maintain high levels of focus and prevent burnout."),
    Strategy(description="Designate a specific workspace in your home that is free from distractions and tailored for productivity, perhaps incorporating elements that inspire you."),
    Strategy(description="Adopt a minimalistic approach by decluttering your workspace to reduce distractions and enhance focus while working from home."),
])

mutations = StrategiesList(strategies=[
    Strategy(description="Study quantum computing."),
    Strategy(description="Create difficult paintings for NY hipsters."),
    Strategy(description="Increase GPD of Cameroon wtih hulla hopping."),
])

all_strategies = strategies.strategies + mutations.strategies
random.shuffle(all_strategies)

print(all_strategies)

for i, strategy in enumerate(all_strategies, start=1):
	print(f"{i}. {strategy.description}")