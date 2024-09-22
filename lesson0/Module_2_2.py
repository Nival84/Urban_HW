first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second == third:
    print('Кол-во равных чисел:',3)
elif first == second != third or third == first != second or second == third != first:
    print('Кол-во равных чисел:',2)
elif first != second != third:
    print('Кол-во равных чисел:',0)
