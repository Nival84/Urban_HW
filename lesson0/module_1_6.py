#part1
my_dict = {"Alex": 1984, 'Dima': 1994}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Anna'))
my_dict.update({'Sasha': 1899, "Egor": 1905})
Dvalue = my_dict.pop('Alex')
print(Dvalue)
print(my_dict)
#part 2
my_set = {1, 2, 3, 4, 4, 3, 2, 1, 'string', 'string', (True, False)}
print(my_set)
my_set.discard((True, False))
my_set.add("We God in trust".upper())
my_set.add(list['pop', 'rock'])
print(my_set)

