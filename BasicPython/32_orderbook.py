import json


def read_file(filename) -> dict:
    with open(filename) as f:
        data = json.load(f)
    return data


def process_data(raw_data):
    orderbook = []
    for bid, ask in zip(raw_data['highbid'], raw_data['lowask']):
        orderbook.append((bid['rate'], bid['amount'],
                         ask['rate'], ask['amount']))
    return orderbook


def display_orderbook(orderbook):
    print(f'{"Bid Volumn":^20}{"Bid Rate":^20}{
          "Ark Rate":^20}{"Ask Volumn":^20}')
    for bv, br, ar, av in orderbook:
        print(f'{bv:^20}{br:^20}{ar:^20}{av:^20}')


def main():
    raw_data: dict = read_file("orderbook.json")
    orderbook = process_data(raw_data)
    display_orderbook(orderbook)


if __name__ == "__main__":
    main()
