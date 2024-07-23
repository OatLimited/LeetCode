list_1 = input("Enter first list : ")
list_1 = [int(i) for i in list_1.split()]
list_2 = input("Enter second list : ")
list_2 = [int(i) for i in list_2.split()]
list_sum = []
for m , n in zip(list_1,list_2):
    list_sum.append(m + n)
print("sum is ", list_sum)