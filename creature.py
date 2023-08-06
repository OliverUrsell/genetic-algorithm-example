import functools
import random
from typing import List, Optional

from constants import representation_length, mutation_probability


class Creature:
    """A representation of the binary this creature represents as a list of length defined in constants.py"""
    _representation: List[bool]

    def __init__(self, representation: Optional[List[bool]] = None):
        # Initialise a creature with the given representation, if None create a random representation
        if representation is not None:
            self._representation = representation
        else:
            self._representation = [random.choice([True, False]) for _ in range(representation_length)]

    def __repr__(self):
        """Ensures that creatures are represented correctly when converting other objects, such as lists, to a string"""
        return self.__str__()

    def __str__(self):
        """Represent the representation list as a binary string"""
        return functools.reduce(lambda acc, val: acc + ("1" if val else "0"), self._representation, "")

    def get_representation(self) -> List[bool]:
        return self._representation

    @staticmethod
    def combine_single_genes(creature_1_gene: bool, creature_2_gene: bool):
        if random.random() < mutation_probability:
            return random.choice([False, True])
        else:
            return random.choice([creature_1_gene, creature_2_gene])

    @staticmethod
    def combine(creature_1, creature_2):
        """Combines the genotypes of two creatures to create their child gene"""
        return Creature(
            representation=[
                Creature.combine_single_genes(creature_1.get_representation()[i], creature_2.get_representation()[i])
                for i in range(representation_length)
            ]
        )


if __name__ == '__main__':
    print("This file should not be run as main, run main.py instead")
