# Входной массив
lst = [6]

# Проверка на пустой массив
if len(lst) == 0:
    result = 0
else:
    # Инициализация переменной для суммы элементов с чётными индексами
    even_index_sum = 0

    # Проход по элементам массива
    for i in range(len(lst)):
        # Проверка на чётность индекса
        if i % 2 == 0:
            even_index_sum += lst[i]

    # Умножение суммы на последний элемент массива
    result = even_index_sum * lst[-1]


print(result)  # Результат