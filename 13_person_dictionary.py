person_dict = {'id' : 1 , 
               'name' : 'Oat' , 
               'date' : '05/11/2000'}
persons_list = []
for i in range(2):
    for key in person_dict.keys():
        person_dict[key] = input(f'{key} input : ')
    persons_list.append(person_dict.copy())

for person in persons_list:
    for key, value in person.items():
        print(f'{key} : {value}')