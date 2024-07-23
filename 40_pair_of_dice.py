
import random


class PairOfDice:
    def __init__(self) -> None:
        self._red_die = 6
        self._blue_die = 12
        self.redvalue = 0
        self.bluevalue = 0

    def roll(self):
        self.redvalue = random.randint(1, self._red_die)
        self.bluevalue = random.randint(1, self._blue_die)

    def sum(self):
        return (self.redvalue + self.bluevalue)


def main():
    pair_of_dice = PairOfDice()
    active = True
    while active:
        pair_of_dice.roll()
        player1 = pair_of_dice.sum()
        print(f'Player 1 : {player1}')
        pair_of_dice.roll()
        player2 = pair_of_dice.sum()
        print(f'Player 2 : {player2}')
        if player1 > player2:
            print("Player 1 WIN!!")
        elif player1 == player2:
            print("TIE")
        else:
            print("Player 2 WIN!!")
        stopper = input("Do you want to play again. y?  :  ")
        if stopper != 'y':
            break


if __name__ == "__main__":
    main()
