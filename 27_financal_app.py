def future_invesment_value(amount, monthly_interest_rate, years=30):
    years = years*12
    future_value = amount * (1 + monthly_interest_rate)**years
    return future_value


def main():
    invest = int(input("The amount invested: "))
    annual = int(input("Annual interest rate: "))
    annual = (annual/100)/12
    for i in range(1, 31):
        print(f'year {i} : Future value {
              future_invesment_value(invest, annual, i)}')


if __name__ == "__main__":
    main()
