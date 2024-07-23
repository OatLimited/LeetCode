from unittest import result


def readfile(filename):
    data = []
    with open(filename, newline="") as f:
        data = f.read().splitlines()
    return data


def process_data(raw_data):
    result = []
    car = []
    for i in raw_data:
        garage = i.split(",")
        mgr = 100/float(garage[1])
        result.append(mgr)
        car.append(garage[0])
    return result, car


def main():
    raw_data = readfile(
        "/Users/limited/Documents/NIDA/CI4003/lecture4/mileage.txt")
    show: tuple = process_data(raw_data)
    car = show[1]
    mgr = show[0]
    print(f'{'Car':^20}{'MGR':^20}')
    print(f'---'*20)
    for x, y in zip(car, mgr):
        print(f'{x:^20}{y:^20}')


if __name__ == "__main__":
    main()
