from random import randint, choice

def randon_dice():
    return randint(1,6) , randint(1,6)

def main():
    for i in range(10):
        print(randon_dice())

if __name__ == '__main__' :
    main()