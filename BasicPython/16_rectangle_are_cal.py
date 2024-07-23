def rec_area(width:int,height:int) ->int :
    area = width * height
    return area

def main():
    input1 = int(input('width : '))
    input2 = int(input('height : '))
    area = rec_area(input1,input2)
    print(f"result is : {area}")


if __name__ == '__main__' :
    main()