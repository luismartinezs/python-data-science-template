import ell
from pydantic import BaseModel, Field
from typing import List
from prompts import zero_shot_cot_user_message
from setup import ControlTheoryInput
ell.init(store="./logdir")


class Strategy(BaseModel):
    description: str = Field(
        description="A brief one or two sentence description of the strategy"
    )


class StrategiesList(BaseModel):
    strategies: List[Strategy] = Field(
        description="A list of strategies to solve the problem"
    )


@ell.complex(model="gpt-4o-mini", response_format=StrategiesList)
def generate_strategies(
    user_input: ControlTheoryInput
):
    return [
        ell.system(
            """You are Leonard, a expert AI strategy generator. Given a problem, context, and constraints, you need to return a list of coarsely defined strategies to solve it. Maximize the variability of the strategies, propose a set of wildly different ideas. Provide at least 10 entries."""
        ),
        zero_shot_cot_user_message(
            f"""Help me brainstorm strategies to solve the following problem: {user_input.problem}
        Context: {user_input.context}
        Constraints: {'None' if not user_input.constraints else ', '.join(user_input.constraints)}
        """
        ),
    ]


@ell.complex(model="gpt-4o-mini", response_format=StrategiesList)
def generate_mutations(strategies: StrategiesList):
    return [
        ell.system(
            """You are Leonard, a expert AI strategy generator. Given a list of strategies, you need to return a list of mutations to the strategies provided by the user. These would be mutations in the context of Evolutionary Strategy. A mutation is a small change to a strategy, i.e. given a strategy composed of N aspects, a mutation changes one and leaves the rest intact. Provide at least 10 mutations."""
        ),
        zero_shot_cot_user_message(
            f"""Help me brainstorm mutations to the following strategies: {strategies.strategies}"""
        ),
    ]


@ell.complex(model="gpt-4o-mini", response_format=StrategiesList)
def generate_recombinations(strategies: StrategiesList):
    return [
        ell.system(
            """You are Leonard, an expert AI strategy generator. Given a list of strategies, you need to return a list of recombinations of the strategies provided by the user. These would be recombinations in the context of Evolutionary Strategy. A recombination takes two parent strategies and generates an "offspring" that combines characteristics of both. Provide at least 10 recombinations."""
        ),
        zero_shot_cot_user_message(
            f"""Help me brainstorm recombinations of the following strategies: {strategies.strategies}
            For each recombination, select two parent strategies and combine their characteristics to create a new strategy."""
        ),
    ]


# Export the generate_strategies function
__all__ = ["generate_strategies", "generate_mutations", "generate_recombinations"]
