input_number = input("Enter list of number : ")
input_number = input_number.split()
input_number = [int(i) for i in input_number]
sum_i = 0
for i in input_number :
    sum_i = sum_i + i
print(sum_i)