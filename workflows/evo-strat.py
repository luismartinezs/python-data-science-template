import random
import openai
import os
import re
import json
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure your API key is correctly set

# Set up logging to a file (append mode)
logging.basicConfig(
    filename="evolution.log",
    filemode="a",  # Append mode
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def generate_strategies(problem_description, num_strategies=10):
    """
    Generates an initial population of candidate strategies using OpenAI.
    """
    logging.info(f"Generating {num_strategies} strategies for the problem.")
    prompt = f"""
You are a helpful assistant tasked with brainstorming creative solutions to problems.

Problem:
{problem_description}

Please provide exactly {num_strategies} distinct and well-defined strategies to address this problem. Each strategy should be concise and described in one sentence.

Respond in JSON format as a list of strings, e.g.,
[
  "Strategy 1 description.",
  "Strategy 2 description.",
  "Strategy 3 description."
]
"""
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",  # Use a suitable chat model
        messages=[{"role": "system", "content": prompt}],
        max_tokens=1000,
        temperature=0.7,
    )
    content = response.choices[0].message.content.strip()
    logging.info(f"Received response:\n{content}")

    # Parse the assistant's output into individual strategies
    try:
        strategies = json.loads(content)
        if not isinstance(strategies, list):
            logging.error("Parsed JSON is not a list.")
            raise ValueError("Expected a list of strategies.")
    except (json.JSONDecodeError, ValueError) as e:
        logging.error(f"Error parsing JSON response: {e}")
        # If parsing fails, recursively call the function to try again
        logging.info("Retrying generation of strategies due to parsing error.")
        return generate_strategies(problem_description, num_strategies)

    # Ensure we have the desired number of strategies
    if len(strategies) < num_strategies:
        logging.warning(f"Received only {len(strategies)} strategies. Generating more.")
        additional_strategies = generate_strategies(
            problem_description, num_strategies - len(strategies)
        )
        strategies.extend(additional_strategies)
    elif len(strategies) > num_strategies:
        strategies = strategies[:num_strategies]

    logging.info(f"Final strategies:\n{json.dumps(strategies, indent=2)}")
    return strategies


def evaluate_strategy(strategy, problem_description):
    """
    Estimates the validity of a strategy using OpenAI.
    """
    logging.info(f"Evaluating strategy:\n{strategy}")
    prompt = f"""
You are an expert consultant evaluating strategies to solve problems.

Problem:
{problem_description}

Strategy:
{strategy}

On a scale of 1 to 10, rate the effectiveness of this strategy in solving the problem. Provide only the number.
"""
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=5,
        temperature=0,
    )
    content = response.choices[0].message.content.strip()
    logging.info(f"Received evaluation: {content}")

    try:
        # Extract the number from the assistant's response
        score = int(re.search(r"\d+", content).group())
        if not 1 <= score <= 10:
            raise ValueError("Score out of range")
        logging.info(f"Assigned score: {score}")
        return score
    except (AttributeError, ValueError) as e:
        logging.error(f"Error parsing score: {e}")
        return 5  # Default score if the response is not a valid number


def mutate_strategy(strategy, problem_description):
    """
    Mutates a strategy by making meaningful changes using OpenAI.
    """
    logging.info(f"Mutating strategy:\n{strategy}")
    prompt = f"""
You are a creative assistant tasked with improving strategies.

Original Strategy:
{strategy}

Problem:
{problem_description}

Please provide a new strategy by making a meaningful change to the original strategy. The new strategy should be concise and described in one sentence.
"""
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=100,
        temperature=0.7,
    )
    mutated_strategy = response.choices[0].message.content.strip()
    logging.info(f"Mutated strategy:\n{mutated_strategy}")
    return mutated_strategy


def recombine_strategies(strategy1, strategy2, problem_description):
    """
    Recombines two strategies into a new one using OpenAI.
    """
    logging.info(
        f"Recombining strategies:\nStrategy 1: {strategy1}\nStrategy 2: {strategy2}"
    )
    prompt = f"""
You are an assistant who combines ideas to create innovative solutions.

Problem:
{problem_description}

Strategy 1:
{strategy1}

Strategy 2:
{strategy2}

Please combine elements from both strategies to create a new, coherent strategy that addresses the problem. The new strategy should be concise and described in one sentence.
"""
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=150,
        temperature=0.7,
    )
    recombined_strategy = response.choices[0].message.content.strip()
    logging.info(f"Recombined strategy:\n{recombined_strategy}")
    return recombined_strategy


def evolve_strategies(
    problem_description, generations=10, mutation_rate=0.3, recombination_rate=0.3
):
    """
    Runs the evolutionary strategy for the given number of generations.
    """
    logging.info(
        f"Starting evolution for {generations} generations with mutation rate {mutation_rate} and recombination rate {recombination_rate}"
    )
    population = generate_strategies(problem_description)
    population_size = len(population)

    for generation in range(generations):
        logging.info(f"\n=== Generation {generation+1} ===")
        new_population = []

        # Mutation
        for strategy in population:
            if random.random() < mutation_rate:
                mutated = mutate_strategy(strategy, problem_description)
                new_population.append(mutated)

        # Recombination
        for _ in range(int(len(population) * recombination_rate)):
            strategy1 = random.choice(population)
            strategy2 = random.choice(population)
            recombined = recombine_strategies(strategy1, strategy2, problem_description)
            new_population.append(recombined)

        # Combine old and new populations
        population.extend(new_population)

        # Evaluation and Selection
        scores = {
            strategy: evaluate_strategy(strategy, problem_description)
            for strategy in population
        }

        # Sort strategies based on scores
        sorted_strategies = sorted(
            scores.items(), key=lambda item: item[1], reverse=True
        )
        population = [strategy for strategy, _ in sorted_strategies[:population_size]]

        # Log top strategies
        top_strategies = [strategy for strategy, _ in sorted_strategies[:3]]
        logging.info(
            f"Top strategies of Generation {generation+1}:\n"
            + "\n".join(top_strategies)
        )

    return population


if __name__ == "__main__":
    problem = "Establish a profitable startup that attracts a minimum of 10,000 visitors and generates an average profit of \$0.50 or more per visitor, with a minimum viable product launched within one week."

    # User input
    problem_description = problem
    # Run the evolution
    winning_strategies = evolve_strategies(problem_description)
    # Output
    print("\nWinning strategies:")
    for strategy in winning_strategies:
        print(strategy)
