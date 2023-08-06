from creature import Creature
from evaluation_functions import distance_from_number


def convert_number(num: int):
    # Create a randomly represented creature and print its representation
    # This creature represents 172
    c1 = Creature([False, False, True, False, True, False, True, True, False, False])
    print(distance_from_number(c1, num))


if __name__ == '__main__':
    convert_number(10)
