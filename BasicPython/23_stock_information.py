import csv
def readfile(filename: str):
    with open(filename, newline='') as f:
                reader = csv.DictReader(f)
                data = [row for row in reader]
                return data

def getsymble(data):
    result = {}
    symble_list = [line["symbol"] for line in data]
    for key, value in zip(symble_list, data):
          result[key] = value
    return result      
          
def main():
    raw_data = readfile("/Users/limited/Documents/NIDA/CI4003/lecture4/dow.csv")
    data = getsymble(raw_data)
    print("-"*50)
    for i in data.keys():
          print(i,end= " ")
    print("\n")
    value = input("please input symble : ")
    for key,value in data[value.upper()].items():
          print(f'{key} : {value}')
          

if __name__ == '__main__':
    main()