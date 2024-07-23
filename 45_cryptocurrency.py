import json


class Cryptocurrency:
    def __init__(self) -> None:
        self.cryptos = {}

    def readfile(self):
        with open("cryptocurrency.json", 'r') as f:
            self.cryptos = json.load(f)
        return self.cryptos

    def register(self, symbol, name, amount):
        self.cryptos[symbol] = [name, amount]

    def get_data(self):
        return self.cryptos


class Portfolio:
    def __init__(self, data) -> None:
        self.crypto = data

    def add(self, symbol, amount):
        self.crypto[symbol][1] += amount

    def remove(self, symbol, amount):
        self.crypto[symbol][1] -= amount
        if self.crypto[symbol][1] <= 0:
            del self.crypto[symbol]

    def display(self) -> str:
        for k, y in self.crypto.items():
            print(f'{k} : {y[0]}  {y[1]}')

    def save(self):
        with open("cryptocurrency.json", 'w') as f:
            json.dump(self.crypto, f)


def main():
    cryptocurrency = Cryptocurrency()
    print('----'*20)
    print("Checking... your portfolio")
    try:
        data = cryptocurrency.readfile()
        print("loading success")
    except:
        print("Cant find your port need to register your port")
        while True:
            symbol = input('Symbol: ')
            name = input('Name: ')
            amount = int(input('Amount :'))
            cryptocurrency.register(symbol, name, amount)
            print('Register complete !!')
            choice = input("Add another cryto (y/n)")
            if choice == 'n':
                break
    data = cryptocurrency.get_data()
    data = {'AAPL': ['apple', 300], 'NVID': [
        'Nvidia', 500], 'SONY': ['sony', 300]}
    portfolio = Portfolio(data)
    while True:
        print('----'*20)
        print('1.Add cryptocurrency : ')
        print("2.Remove crytocurrency :")
        print("3.Display portfolio ")
        print("4.Quit program")
        print('----'*20)
        choice = int(input('Your choice : '))
        print('----'*20)
        if choice == 1:
            symbol = input('Symbol :')
            amount = int(input('Amount :'))
            portfolio.add(symbol, amount)
        elif choice == 2:
            symbol = input('Symbol :')
            amount = int(input('Amount :'))
            portfolio.remove(symbol, amount)
        elif choice == 3:
            portfolio.display()
        else:
            portfolio.save()
            break


if __name__ == "__main__":
    main()
