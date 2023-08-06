from creature import Creature


def convert_number(num: int):
    # Create a randomly represented creature and print its representation
    c1 = Creature([False, False, True, False, True, False, True, True, False, False])
    print(str(c1))

    c2 = Creature([True, True, False, True, True, True, True, False, True, False])
    print(str(c2))

    c3 = Creature.combine(c1, c2)
    print(str(c3))


if __name__ == '__main__':
    convert_number(10)
