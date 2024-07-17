import string

# Ввод строки от пользователя
user_input = input("Введите строку: ")

# Удаление знаков препинания и пробелов
user_input = user_input.translate(str.maketrans('', '', string.punctuation))

# Изменение каждого отдельного слова, что бы оно начиналось с большой буквы
words = [word.capitalize() for word in user_input.split()]

# Объединение слов в одну строку с добавлением символа '#' в начале
hashtag = '#' + ''.join(words)

# Ограничение длины хэш-тега до 140 символов
if len(hashtag) > 140:
    hashtag = hashtag[:140]

# Вывод результата
print(hashtag)
