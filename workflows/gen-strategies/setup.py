import ell
from pydantic import BaseModel, Field
from typing import List
from prompts import zero_shot_cot_user_message

ell.init(store="./logdir")


class ControlTheoryInput(BaseModel):
    problem: str = Field(description="The problem to solve or outcome to achieve")
    context: str = Field(description="Current user situation or starting point")
    constraints: List[str] | None = Field(
        description="User-defined constraints", default=None
    )


class ControlTheoryOutput(BaseModel):
    goal: str = Field(description="Defined goal or outcome (point B)")
    starting_point: str = Field(description="Defined starting point (point A)")
    state_variables: List[str] = Field(
        description="State variables (x): These describe the system's current state and represent measurable quantities that change over time. They must be measurable and observable."
    )
    control_variables: List[str] = Field(
        description="Control variables (u): These are the inputs or levers that can be adjusted to influence the system's state. actions that drive the evolution of the system. Control variables directly affect the state variables and their future trajectory."
    )


# not useful
@ell.complex(model="gpt-4o-mini")
def get_ideal_outcome(input_data: ControlTheoryInput):
    return [
        ell.system(
            "You are Joseph, an extremely creative and imaginative AI. You excel at helping people reinterpret goals and aspirations in a way that makes them as good as possible. You excel at helping people image what is the best case scenario, the ideal outcome."
        ),
        ell.user(
            f"I have this problem that I want to solve: {input_data.problem}. Help me image the best possible scenario which solves this problem. The perfect outcome. Keep your answer concise and constrained to 2 or 3 sentences.\n\n[IDEAL OUTCOME]\n<my-ideal-outcome>: write your answer here, starting with 'The ideal outcome is...')"
        ),
    ]


@ell.complex(model="gpt-4o-mini", response_format=ControlTheoryOutput)
def get_variables(input_data: ControlTheoryInput):
    return [
        ell.system(
            "You are Travis, an expert in control theory applied to strategy optimization. Given a problem, context, and constraints, analyze the situation and provide a control theory-based output."
        ),
        zero_shot_cot_user_message(
            f"""Based on the following input, provide a detailed and accurate control theory analysis:
    Problem: {input_data.problem}
    Context: {input_data.context}
    Constraints: {'None' if not input_data.constraints else ', '.join(input_data.constraints)}"""
        ),
    ]


class DynamicsEquations(BaseModel):
    equations: List[str] = Field(
        description="Dynamics equations (f) describing the relationships between variables"
    )


@ell.complex(model="gpt-4o-mini", response_format=DynamicsEquations)
def get_relations(input_data: ControlTheoryInput, variables: ControlTheoryOutput):
    return [
        ell.system(
            "You are Travis, an expert in control theory applied to strategy optimization. Given a problem, context, constraints, and variables, analyze the situation and provide dynamics equations describing the relationships between variables. You keep things relatively simple as your answer is based on reasoned speculation."
        ),
        zero_shot_cot_user_message(
            f"""Based on the following input and variables, provide dynamics equations (f) that describe how the state variables change over time in response to the control variables:
    Problem: {input_data.problem}
    Context: {input_data.context}
    Constraints: {'None' if not input_data.constraints else ', '.join(input_data.constraints)}
    State Variables: {', '.join(variables.state_variables)}
    Control Variables: {', '.join(variables.control_variables)}

    Please provide a list of equations, each as a string, describing the relationships between these variables."""
        ),
    ]


def apply_control_theory(input_data: ControlTheoryInput):
    variables = get_variables(input_data)
    relations = get_relations(input_data, variables.parsed)
    return [variables.parsed, relations.parsed]


# Export the apply_control_theory function
__all__ = ["apply_control_theory", "get_ideal_outcome"]
