# Урок 5: генераторы и работа с памятью

import sys


# Обычная функция строит ВЕСЬ список в памяти сразу
def squares_list(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result


# Генератор считает значения по одному, только когда их просят
def squares_gen(n):
    for i in range(n):
        # yield ставит функцию на паузу и отдает значение
        yield i * i


# Сравниваем размер в памяти
big_list = squares_list(100_000)
big_gen = squares_gen(100_000)
print("список:", sys.getsizeof(big_list), "байт")
print("генератор:", sys.getsizeof(big_gen), "байт")

# Генератор можно обойти только один раз
print(sum(big_gen))
print(sum(big_gen))  # уже пустой, сумма 0

# Генераторное выражение: как списковое включение, но со скобками ()
lazy = (i * i for i in range(10))
print(list(lazy))

# Генераторы можно соединять в конвейер: данные текут по одному элементу,
# память не растет от размера данных
numbers = range(1_000_000)
evens = (n for n in numbers if n % 2 == 0)
squared = (n * n for n in evens)
# Считается только когда дошли до sum - до этого ни одного вычисления
print(sum(squared))
