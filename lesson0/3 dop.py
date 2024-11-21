def calculate_structure_sum(data_structure):
    total_sum = 0

    # Обрабатываем каждый элемент в структуре данных
    for item in data_structure:
        if isinstance(item, int):  # Если это число, добавляем его
            total_sum += item
        elif isinstance(item, str):  # Если это строка, добавляем ее длину
            total_sum += len(item)
        elif isinstance(item, dict):  # Если это словарь, обрабатываем ключи и значения
            for key, value in item.items():
                total_sum += calculate_structure_sum([key])  # Обрабатываем ключи
                total_sum += calculate_structure_sum([value])  # Обрабатываем значения
        elif isinstance(item, tuple):  # Если это кортеж, обрабатываем элементы
            total_sum += calculate_structure_sum(item)
        elif isinstance(item, list):  # Если это список, обрабатываем элементы
            total_sum += calculate_structure_sum(item)
        elif isinstance(item, set):  # Если это множество, обрабатываем элементы
            total_sum += calculate_structure_sum(list(item))

    return total_sum

data_structure = [

[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)