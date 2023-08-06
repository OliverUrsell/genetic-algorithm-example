import random
from typing import List

from constants import population_size
from creature import Creature


def choose_random(population: List[Creature]) -> List[Creature]:
    while len(population) != population_size:
        population.append(Creature.combine(*random.choices(population, k=2)))

    return population
