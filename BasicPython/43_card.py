import random


class Card:
    def __init__(self) -> None:
        self.suits = ["Heart", "Spades", "Clubs", "Diamonds"]
        self.ranks = ['2', '3', '4', '5', '6', '7',
                      '8', '9', '10', 'K', 'Q', 'J', 'A']
        self.deck_list = []

    def deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                card = suit + " " + rank
                for i in range(3):
                    self.deck_list.append(card)
        random.shuffle(self.deck_list)

    def draw(self):
        return random.choice(self.deck_list)


def main():
    card = Card()
    print(f'{'______'*20}')
    print("1 shuffle deck")
    print("2 draw card")
    print("q to quit")
    print(f'{'______'*20}')
    while True:
        user_input = input("You choice : ")
        if user_input == '1':
            card.deck()
        elif user_input == '2':
            print(card.draw())
        else:
            break


if __name__ == "__main__":
    main()
