import random


def random_whiteball():
    whiteball = random.sample(range(1, 61), k=5)
    return whiteball


def random_powerball():
    powerball = random.randint(1, 36)
    return powerball


def main():
    whiteball = random_whiteball()

    for i in whiteball:
        print(i, end=" ")
    print("\n")
    print(random_powerball())


if __name__ == '__main__':
    main()
