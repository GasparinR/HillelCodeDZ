import re


def first_word(text):
    """ Поиск первого слова """
    # Убираем начальные и конечные символы пунктуации, пробелы
    text = text.strip(" ,.")

    # Используем регулярное выражение, чтобы найти первое слово
    match = re.search(r"[a-zA-Z']+", text)

    if match:
        print(match.group(0))
        return match.group(0)
    return ""


# Тесты
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("hello.World") == "hello", 'Test6'

print('OK')
