import random
from turtle import position
import numpy as np


def custom_suffle(number):
    # create empty_array
    n = len(number)
    empty_array = [None for i in range(n)]
    # create random position list without duplicate value
    position = random.sample(range(0, n), n)
    # put number, index follow by position list
    for i in range(len(number)):
        empty_array[position[i]] = number[i]
    return empty_array


def main():
    # inital varible n
    n = 50
    # create list to contain number was generated
    number = [random.randrange(0, n-1) for i in range(n)]
    print("Number before suffle : ")
    print(number)
    print("After suffle : ")
    print(custom_suffle(number))

    # Big O = O(n)


if __name__ == "__main__":
    main()
