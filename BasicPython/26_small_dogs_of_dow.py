import csv


def readfile(filename: str):
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        return data


def display(raw_data):
    yield_dict = {}
    for line in raw_data:
        yield_dict[line["company"]] = line["price_end"]
    return yield_dict


def main():
    raw_data = readfile(
        "/Users/limited/Documents/NIDA/CI4003/lecture4/dow.csv")
    result = display(raw_data)
    top5 = sorted(result.items(), key=lambda x: float(x[1]))
    for i in top5:
        print(i)


if __name__ == "__main__":
    main()
