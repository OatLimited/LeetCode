import csv


def readfile(filename: str):
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        return data


def best_worse_stock(raw_data: list):
    for line in raw_data:
        percentage = (float(
            line["price_begin"]) - float(line["price_end"])) / (float(line["price_begin"])*100)
        line["percentage"] = percentage
    return raw_data


def display(cal_result):
    display_dict = {}
    for line in cal_result:
        display_dict[line["company"]] = float(line["percentage"])
    for key, value in sorted(display_dict.items()):
        display_dict[key] = value
    return display_dict


def main():
    raw_data = readfile(
        "/Users/limited/Documents/NIDA/CI4003/lecture4/dow.csv")
    cal_result = best_worse_stock(raw_data)
    result: dict = display(cal_result)
    key: list = [i for i in result.keys()]
    print(f"the best stock is {key[0]} : {result[key[0]]}")
    print(f"the worse stock is {key[-1]} : {result[key[-1]]}")


if __name__ == "__main__":
    main()
