import string
import keyword

# Ввод строки пользователем
user_input = input("Введите строку: ")

# Проверка на цифру в начале строки
if user_input[0].isdigit():
    print(False)
else:
    # Проверка на заглавные буквы
    if any(char.isupper() for char in user_input):
        print(False)
    else:
        # Проверка на наличие недопустимых символов
        invalid_chars = set(string.punctuation.replace('_', '') + ' ')
        if any(char in invalid_chars for char in user_input):
            print(False)
        else:
            # Проверка на зарегистрированные слова
            if user_input in keyword.kwlist:
                print(False)
            else:
                # Проверка на количество нижних подчеркиваний
                if user_input.count('_') > 1:
                    print(False)
                else:
                    print(True)
