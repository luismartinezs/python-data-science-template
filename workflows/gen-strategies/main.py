import random
from evolution import (
    generate_strategies,
    generate_mutations,
    generate_recombinations,
    StrategiesList,
    Strategy,
)
from setup import apply_control_theory, ControlTheoryInput, get_ideal_outcome
from prompts import zero_shot_cot_user_message

user_input = ControlTheoryInput(
    problem="How to optimize productivity in a sustainable way, while working from home as a developer?",
    context="I am a 40 year old developer. I work alone from home. I do not have family. I can productively work between 3 and 5 hours per day.",
    constraints=["I need to increase and optimize my productivity significantly."],
)

# messages = zero_shot_cot_user_message(
#     f"""Based on the following input, provide a detailed and accurate control theory analysis:
#     Problem: {user_input.problem}
#     Context: {user_input.context}
#     Constraints: {'None' if not user_input.constraints else ', '.join(user_input.constraints)}"""
# )

# print(messages)

# [variables, relations] = apply_control_theory(user_input)

# print("Control Theory Analysis:")
# print(f"Goal: {variables.goal}")
# print(f"Starting Point: {variables.starting_point}")
# print("\nState Variables:")
# for var in variables.state_variables:
#     print(f"- {var}")
# print("\nControl Variables:")
# for var in variables.control_variables:
#     print(f"- {var}")

# print("\nRelations:")
# for rel in relations:
#     print(f"- {rel}")

# ideal_outcome = get_ideal_outcome(user_input)

# print(ideal_outcome.text)

# strategies_message = generate_strategies(user_input)
# strategies = strategies_message.parsed

# mutations_message = generate_mutations(strategies)
# mutations = mutations_message.parsed

# recombinations_message = generate_recombinations(strategies)
# recombinations = recombinations_message.parsed

# all_strategies = strategies.strategies + mutations.strategies + recombinations.strategies
# random.shuffle(all_strategies)

# # print("All Strategies:")
# for i, strategy in enumerate(all_strategies, 1):
#     print(f"{i}. {strategy.description}")

