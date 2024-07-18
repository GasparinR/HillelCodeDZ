import string

input_str = input("Write 2 letters separated by a hyphen: ")
start_char, end_char = input_str.split('-')

# Получить индексы букв в string.ascii_letters
start_index = string.ascii_letters.index(start_char)
end_index = string.ascii_letters.index(end_char)

result = string.ascii_letters[start_index:end_index + 1]

print(result)
