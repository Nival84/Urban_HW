name = [1, 2, 3, 4, 5].index(3, 0)
print(name)
# name_2 = 'добро пожаловать на борт'.index('о', 2, 5)
# print(name_2)
#
# #Определить порядковый номер значения в строке
# s = 'abcdefg3423424245'
# for i in range(999):
#     print(i, s[i])
#
# name = "test"
# for index, char in enumerate(name):
#  print(f"{char} - {index}")
# from lesson0.module_1_4 import my_string
#
# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# list_student = list(students)
# list_student.sort()
# a1 = sum(grades[0])/len(grades[0])
# a2 = sum(grades[1])/len(grades[1])
# a3 = sum(grades[2])/len(grades[2])
# a4 = sum(grades[3])/len(grades[3])
# a5 = sum(grades[4])/len(grades[4])
# V1 = {list_student[0]: a1, list_student[1]: a2, list_student[2]: a3, list_student[3]: a4, list_student[4]: a5}
# print(V1)
# var = 'Hello World!'
# print(var[2:7:2])
# son_age = 5
# my_age = "30"
# print(son_age + my_age)
# son_age = 5
# my_age = "30"
# print(son_age + int(my_age))
# son_age = 5
# my_age = "30"
# print(son_age * my_age)
# my_list = ['apple', 'banana', 'peach']
# my_list[0] = ['watermelon']
# print(my_list)
# my_tuple = ('apple', 'banana', 'peach')
# my_tuple[0] = 'watermelon'
# print(my_tuple)
# Как получить год рождения Александра в следующем словаре
# birth_date = {'Олег': 1995, 'Никита': 1978, 'Алексей': 2002, 'Александр': 1989}
# print(birth_date['Александр'])
# Что выведет следующая программа:
# my_set = {10, 20, 30}
# my_set.add(20)
# print(my_set)
# name = "tSDAADSDAest"
# for index, char in enumerate(name):
# print(f"{char} - {index}")
# s = 'abcdefghijklm12345'
# for i in range(99):
#     print(i, s[i])
# a = 45
# b = 30
# print(a//b)
# / деление
# // целое деление
# % остаток от деления
# * умножение
# ** возведение в степень
# name = input('Ваше имя')
# print('privey', ',', name)
# name = input('Ваше имя')
# print(f'Здравствуйте, {name}')
# name1 = 'вторник'
# name2 = "понедельник"
# print(f'{name1}      {name2}')
#условные операторы
# a = 10
# b = 7
# c = 10
# if a==b or b==c or b==c:
#     print(2)
# elif a==b==c:
#     print(3)
# else:
#     print(0)
# a = int(input('Введите 1 число: '))
# b = int(input('Введите 2 число: '))
# if a>b:
#     print(a)
# if b>a:
#     print(b)
#     print(type(b))
# a = []
# a.append('a')
# a.append('b')
# a.append('c')
# print(a)
# print(a[-1])
# print(a[0])
# print(a[1:3:2])
# print(a[::-1])
# a = {1,1,2,2,3, 'a','b', True, False, 0}
# print(a)
# from time import struct_time
#
# from lesson0.dop import grades
#
# grades1 = [[5, 3, 3, 5, 4], [2, 2, 2, 3]]
# students = {'Johnny', 'Bilbo'}
#
# students_sort = sorted(students)
# grades_m = []
# for num in grades:
#     s = sum(num)/len(num)
#     grades_m.append(s)
#
#
#
# dict1 = dict(zip(students_sort, grades_m))
# print(dict1)

# a = 9
# b = 5
# print(a/b)
# print(a//b)
# print(a%b)
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        _list = []
        matrix.append(_list)
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(3, 4, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

