number = int(input("Введите целое число: "))

# Преобразование отрицательного числа в положительное
if number < 0:
    number = abs(number)

# Основной процесс
while number > 9:
    temp = number
    result = 1
    while temp > 0:
        result *= temp % 10
        temp //= 10
    number = result

# Вывод результата
print("Результат:", number)
