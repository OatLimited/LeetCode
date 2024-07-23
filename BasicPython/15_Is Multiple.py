def is_multiple(number1:int,number2:int):
    return number2 % number1 == 0


def main():
    number1 = int(input("Please input number1 :"))
    number2 = int(input("Please input number2 :"))
    print(is_multiple(number1,number2))

if __name__ == '__main__' :
    main()