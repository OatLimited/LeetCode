def triangle(side1: int, side2: int, side3: int):
    return (side1 + side2 > side3) & (side1 + side3 > side2) &  (side2 + side3 > side1)


def main():
    input1 = int(input('Side 1 : '))
    input2 = int(input('Side 2 : '))
    input3 = int(input('Side 3 : '))
    result = triangle(input1, input2, input3)
    print(f'Is this triangle : {result}')

if __name__ == "__main__" :
    main()