from sys import activate_stack_trampoline


class Account:
    def __init__(self, amount) -> None:
        self.amount = amount

    def deposit(self, money, amount):
        self.amount = amount + money
        return self.amount

    def withdraw(self, money):
        if money <= self.amount:
            return (self.amount - money)
        return f'You havent enough money for withdraw'

    def check_amount(self):
        return self.amount


class SavingsAccount(Account):
    def __init__(self, amount, rate=0.05) -> None:
        super().__init__(amount)
        self.rate = rate

    def calculate_rate(self, amount):
        return (amount * self.rate)


class CheckingAccount(Account):
    def __init__(self, amount, limit) -> None:
        super().__init__(amount)
        self.limit = limit

    def withdraw(self, amount, money):
        if amount - money <= self.limit:
            return (amount - money)
        return 0


def main():
    amount = int(input("Input your money : "))
    account = Account(amount)
    save = SavingsAccount(amount)
    check = CheckingAccount(amount, 50000)
    active = True
    while active:
        print(f'{'---'*20}')
        print('1 : deposite')
        print('2 : withdraw')
        print('3 : check interest')
        print('4 : quit')
        user = int(input("Choose : "))
        if user == 1:
            depo = int(input("input you deposit : "))
            amount = account.deposit(amount, depo)
            print(amount)
        elif user == 2:
            withdraw = int(input("input money you want to withdraw : "))
            amount = account.withdraw(amount, withdraw)
            print(amount)
        elif user == 3:
            amount += save.calculate_rate(amount)
            print(amount)
        else :
            break


if __name__ == "__main__":
    main()
