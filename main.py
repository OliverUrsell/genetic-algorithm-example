from combination_functions import choose_random
from constants import culling_proportion, population_size, generations
from creature import Creature
from evaluation_functions import distance_from_number


def convert_number(num: int):
    # Create a randomly represented creature and print its representation
    population = [Creature() for _ in range(population_size)]

    print(f"Trying to create a creature to match the number {str(bin(num))[2:]} - {num}\n")

    for generation_number in range(generations):
        print(f"Generation {generation_number}")

        # Sort the population based on an evaluation function
        population.sort(key=lambda c: distance_from_number(c, num))

        print(f"Best creature: {population[0]} - {int(str(population[0]), 2)}")
        print(f"Worst creature: {population[-1]} - {int(str(population[-1]), 2)}")

        # Cull a proportion of the population
        population = population[:int(len(population)*culling_proportion)]

        # Combine the creatures according to a combination function to create the population for the next generation
        population = choose_random(population)

        print("")


if __name__ == '__main__':
    convert_number(10)
