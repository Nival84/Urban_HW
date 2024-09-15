name = [1, 2, 3, 4, 5].index(3, 0)
print(name)
name_2 = 'добро пожаловать на борт'.index('о', 2, 5)
print(name_2)

#Определить порядковый номер значения в строке
s = 'abcdefg3423424245'
for i in range(999):
    print(i, s[i])

name = "test"
for index, char in enumerate(name):
 print(f"{char} - {index}")