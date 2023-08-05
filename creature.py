import functools
import random
from typing import List, Optional

from constants import representation_length


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


if __name__ == '__main__':
    print("This file should not be run as main, run main.py instead")
