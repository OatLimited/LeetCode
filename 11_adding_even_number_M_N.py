list_1 = input("Enter first list : ")
list_1 = [int(i) for i in list_1.split()]
list_2 = input("Enter second list : ")
list_2 = [int(i) for i in list_2.split()]
sum_value = 0
print('list 1 :',list_1)
print('list 2 :',list_2)
for i in list_1:
    if i % 2 == 0 :
        sum_value += i 
for i in list_2:
    if i % 2 == 0 :
        sum_value += i 
print("sum is ", sum_value)