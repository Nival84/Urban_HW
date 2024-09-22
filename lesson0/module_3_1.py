# def count_calls(): #подсчитывающая вызовы остальных функций.
# def string_info():принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# def is_contain():принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

# Пункты задачи:
# _X_ Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contain(sting, list_to_search):
    count_calls()
    for i in list_to_search:
        return any(substring.lower() in sting.lower() for substring in list_to_search)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contain('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contain('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
