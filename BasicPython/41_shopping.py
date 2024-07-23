from re import sub


class Purchase:
    def __init__(self, price, quantity) -> None:
        self.price = int(price)
        self.quantity = int(quantity)

    def total(self):
        self.total_amount = self.price * self.quantity
        return self.total_amount

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price >= 0:
            self._price = price
        else:
            self._price = 0

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity


class Cart:
    def __init__(self) -> None:
        self.temp_cart = {}
        self.total_cart = []

    def addcart(self, item, quantity, price):
        purchase = Purchase(price, quantity)
        self.temp_cart["Desciption"] = item
        self.temp_cart["Quantity"] = int(quantity)
        self.temp_cart["Price"] = int(price)
        self.temp_cart["Totalline"] = purchase.total()
        self.total_cart.append(self.temp_cart.copy())

    def return_cart(self):
        return self.total_cart


def print_recipt(buy_list):
    print(f'{'Description':<20}{'Qyt':<20}{'UnitPrice':<20}{'Linetotal':<20}')
    print(f'{'----'*20}')
    subtotal = 0
    for i in buy_list:
        purchase = Purchase(i['Quantity'],  i['Price'])
        print(f'{i['Desciption']:<20}{i['Quantity']:<20}{
              i['Price']:<20}{i['Totalline']:<20}')
        subtotal += i['Totalline']
    print(f'{'----'*20}')
    print(f'{'Subtotal':<20}{subtotal:>20}')
    print(f'{'Tax':<20}{subtotal*0.07:>20}')
    print(f'{'Total':<20}{subtotal*1.07:>20}')


def main():
    cart = Cart()
    while True:
        desciption = input("Enter description of article (q to quit) : ")
        if desciption != "q":
            price = int(input("Enter price : "))
            quantity = int(input("Enter quantity : "))
            cart.addcart(desciption, price, quantity)
        else:
            buy_list = cart.return_cart()
            break
    print_recipt(buy_list)


if __name__ == "__main__":
    main()
