def is_palindrome(text):
    text = text.lower()
    text = ''.join(char for char in text if char.isalnum())
    result = text == text[::-1]
    print(f'Is the text "{text}" a palindrome? {result}')
    return result


is_palindrome('A man, a plan, a canal: Panama')
is_palindrome('0P')
is_palindrome('a.')
is_palindrome('g')
is_palindrome('aurora')

print("ОК")
