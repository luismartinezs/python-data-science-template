import random
from deap import base, creator, tools, algorithms


# Define the fitness function
def fitness_function(individual):
    # Simple fitness function: sum of genes
    return (sum(individual),)


# Set up parameters
population_size = 100
gene_length = 10
generations = 50
mutation_rate = 0.1
crossover_rate = 0.5

# Set up DEAP
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, 0, 1)
toolbox.register(
    "individual",
    tools.initRepeat,
    creator.Individual,
    toolbox.attr_float,
    n=gene_length,
)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", fitness_function)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=mutation_rate)
toolbox.register("select", tools.selTournament, tournsize=3)

# Generate initial population
population = toolbox.population(n=population_size)

# Run evolutionary strategy
for generation in range(generations):
    # Evaluate fitness
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit

    # Select the next generation individuals
    offspring = toolbox.select(population, len(population))

    # Clone the selected individuals
    offspring = list(map(toolbox.clone, offspring))

    # Apply crossover and mutation
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < crossover_rate:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

    for mutant in offspring:
        if random.random() < mutation_rate:
            toolbox.mutate(mutant)
            del mutant.fitness.values

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    # Replace the old population by the offspring
    population[:] = offspring

    # Print progress
    best_individual = tools.selBest(population, 1)[0]
    print(
        f"Generation {generation + 1}: Best fitness = {best_individual.fitness.values[0]:.4f}"
    )

# Print final result
best_individual = tools.selBest(population, 1)[0]
print(f"\nFinal best individual: {best_individual}")
print(f"Final best fitness: {best_individual.fitness.values[0]:.4f}")
