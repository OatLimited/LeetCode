
from math import sqrt


class Vector:
    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)

    def magnitude(self):
        return sqrt((self.x ** 2 + self.y ** 2))

    def __str__(self) -> str:
        return f'Vector : {self.x} {self.y} \nmagnitude : {self.magnitude()}'


def main():
    user_input = input("please input coodinate :")
    user_input = user_input.split()
    vector = Vector(user_input[0], user_input[1])
    print(vector)


if __name__ == "__main__":
    main()
