immutable_var = (1,2, True, 'name', [3,4], ["test1"]) #Кортеж не изменин. Менять можно только  обьекты внутри кортежы.
print(immutable_var)
immutable_var[4][0] = 6
immutable_var[5][0] = 'T1'
print(immutable_var)
mutable_list = [1,2,'sort']
print(mutable_list)
mutable_list[2] = '3 sport'
print(mutable_list)
