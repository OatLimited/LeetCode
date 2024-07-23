
def read_file(filename):
    with open(filename) as f:
        reader = f.read()
    return reader


def process_data(data: str):
    result = {}
    data = data.replace(",", "").replace(" ", "").lower()
    for ch in data:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result


def main():

    file = input("please input file: ")
    try:
        raw_data = read_file(file)
        result = process_data(raw_data)
        for key, value in result.items():
            print(f'{key} appear : {value} time')
    except FileNotFoundError as e:
        print(f'File {file} does not exist.Try agian')



if __name__ == "__main__":
    main()
