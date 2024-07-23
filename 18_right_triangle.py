def right_triangle(side1: int, side2: int, side3: int):
    side = sorted([side1, side2, side3], reverse=True)
    return side[0]**2 == side[1]**2 + side[2]**2 
    

def main():
    input1 = int(input('Side 1 : '))
    input2 = int(input('Side 2 : '))
    input3 = int(input('Side 3 : '))
    result : bool = right_triangle(input1, input2, input3)
    print(result)

if __name__ == '__main__':
    main()
