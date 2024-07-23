def counting (text:str) -> int:
    count = {}
    text = text.lower()
    for ch in text:
        if ch in count:
            count[ch] += 1
        else : 
            count[ch] = 1
    return count


def main() :
    strinput = input("Please input text :")
    count:dict = counting(strinput)
    for k, y in count.items():
        print(f'{k} : {y}')
     


if __name__ == '__main__' :
    main()