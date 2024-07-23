from curses import endwin
from unittest import result


def read_file(filename):
    with open(filename) as f:
        raw_data = f.read().splitlines()
    return raw_data


def dict_data(raw_data: str):
    dict_product = {}
    raw_data = raw_data.split(",")
    dict_product['Description'] = raw_data[0]
    dict_product['Quantity'] = int(raw_data[1])
    dict_product['price_per_unit'] = int(raw_data[2])
    dict_product['line_total'] = int(dict_product['Quantity'] *
                                     dict_product['price_per_unit'])
    return dict_product


def sumproduct(product: list):
    total_amount = 0
    for dict_product in product:
        total_amount += dict_product['line_total']
    return total_amount


def display_item(product):
    for key in product[0].keys():
        print(f'{key:^20}', end=" ")
    print("")
    print("----"*20)
    for dict_product in product:
        print(f'{dict_product['Description']:^20}{dict_product['Quantity']:^20}{
              dict_product['price_per_unit']:^20}{dict_product['line_total']:>20}')


def display_invoice(product, totalamount):
    vat = totalamount * 0.07
    display_item(product)
    print("----"*20)
    print(f'{'subtotal':<20}{totalamount:>60}')
    print(f'{'vat':<20}{vat:>60}')
    print(f'{'total':<20}{totalamount + vat:>60}')


def main():
    raw_data = read_file(
        "/Users/limited/Documents/NIDA/CI4003/lecture5/order.txt")
    product = []
    for line in raw_data:
        product.append(dict_data(line))
    total_amount = sumproduct(product)
    display_invoice(product, total_amount)


if __name__ == "__main__":
    main()
