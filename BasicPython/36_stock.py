class Stock:
    def __init__(self, name, symbol, previous_close, last) -> None:
        self.name = name
        self.symbol = symbol
        self.previous_close = int(previous_close)
        self.last = int(last)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    @property
    def previous_close(self):
        return self._previous_close

    @previous_close.setter
    def previous_close(self, previous_close):
        self._previous_close = previous_close

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last):
        self._last = last

    def change(self):
        return (self.last - self.previous_close)

    def pct_change(self):
        return ((self.change()*100)/self.previous_close)


def main():
    name = input("Name : ")
    symbol = input("Symbol : ")
    previous_close = input("Close price : ")
    last = input("Last price : ")
    stock = Stock(name, symbol, previous_close, last)
    print(f'percentage : {stock.pct_change():2f}')
    print(f'chane value : {stock.change()}')


if __name__ == "__main__":
    main()
