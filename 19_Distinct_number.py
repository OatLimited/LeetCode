def distinct_number(set):
    setdict = {}
    for i in set:
        if i in setdict:
            setdict[i] += 1
        else :
            setdict[i] = 1
    return setdict

def main():
    inputnum = str(input('Input set of number :'))
    result: dict = distinct_number(inputnum)
    dispaly = [int(key) for key in result.keys()]
    print(dispaly)



if __name__ == '__main__':
    main()