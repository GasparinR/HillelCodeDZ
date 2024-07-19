# Ввод количества секунд
seconds = int(input("Введите количество секунд: "))

# Проверка, что число в заданном диапазоне
if seconds < 0 or seconds >= 8640000:
    print("Число должно быть больше или равно 0 и менее 8640000")
else:
    # Вычисление дней, часов, минут и секунд
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Определение правильного слова для "день"
    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_word = "дні"
    else:
        day_word = "днів"

    formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    print(formatted_time)
