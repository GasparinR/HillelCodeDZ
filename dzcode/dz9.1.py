def popular_words(text, words):
    # Приводим текст к нижнему регистру и разбиваем его на слова
    text_lower = text.lower()
    text_words = text_lower.split()

    # Создаем словарь для хранения частоты слов
    word_count = {word: 0 for word in words}

    # Подсчитываем частоту слов
    for word in text_words:
        if word in word_count:
            word_count[word] += 1

    # Печатаем результат
    print(word_count)

    return word_count


# Пример использования функции
popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
              ['i', 'was', 'had', 'when'])
