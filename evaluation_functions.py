
from creature import Creature


def distance_from_number(creature: Creature, num: int) -> int:
    """
    Evaluates a creatures genotype as a binary number and returns the difference between that representation and num
    """

    return abs(num - int(str(creature), 2))
