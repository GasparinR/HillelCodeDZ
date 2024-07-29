def is_palindrome(text):
    # Приводим строку к нижнему регистру
    text = text.lower()
    # Оставляем только буквы и цифры
    text = ''.join(char for char in text if char.isalnum())
    # Проверяем, является ли строка палиндромом
    result = text == text[::-1]
    # Выводим результат проверки
    print(f'Is the text "{text}" a palindrome? {result}')
    return result


# Тесты
is_palindrome('A man, a plan, a canal: Panama')
is_palindrome('0P')
is_palindrome('a.')
is_palindrome('g')
is_palindrome('aurora')

print("ОК")
