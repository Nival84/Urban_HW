def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        test1 = []
        matrix.append(test1)
        for j in range(m):
            matrix[i].append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4,2, 13)
print(result1)
print(result2)
print(result3)


n = int(input('Введите кол-во строк: = '))
m = int(input('Введите кол-во столбцов: = '))
value = int(input('Введите значение: = '))
matrix = get_matrix(n, m, value)
print(matrix)

