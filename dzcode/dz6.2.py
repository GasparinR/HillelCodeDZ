# Ввод количества секунд
seconds = int(input("Enter the number of seconds:"))

# Проверка, что число в заданном диапазоне
if seconds < 0 or seconds >= 8640000:
    print("The number must be greater than or equal to 0 and less than 8640000")
else:
    # Вычисление дней, часов, минут и секунд
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Форматирование вывода
    day_word = "days" if days != 1 else "day"
    formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    # Вывод результата
    print(formatted_time)
