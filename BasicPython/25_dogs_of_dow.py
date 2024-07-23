import csv


def readfile(filename: str):
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        return data


def yield_cal(raw_data):
    for line in raw_data:
        if line['dividend'] == '':
            line['dividend'] = 0
        line["yield"] = float(line['dividend'])/float(line['price_end'])*100
    return raw_data


def display(raw_data):
    yield_dict = {}
    for line in raw_data:
        yield_dict[line["company"]] = line["yield"]
    return yield_dict


def main():
    raw_data = readfile(
        "/Users/limited/Documents/NIDA/CI4003/lecture4/dow.csv")
    raw_data = yield_cal(raw_data)
    result = display(raw_data)
    top5 = sorted(result.items(), reverse=True, key=lambda x: x[1])
    for i in range(5):
        print(top5[i])


if __name__ == "__main__":
    main()
