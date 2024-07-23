def commission_rate(sale):
    if sale < 100000:
        sale = sale*0.06
    elif sale < 500000:
        sale = sale*0.08
    elif sale < 1000000:
        sale = sale*0.1
    else:
        sale = sale*0.12
    return sale


def main():
    print("Sale Amount : Commission")
    for i in range(1, 11):
        sale = i * 100000
        result = commission_rate(sale)
        print(f'{sale} : {result}')


if __name__ == "__main__":
    main()
