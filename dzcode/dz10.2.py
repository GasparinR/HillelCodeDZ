import re


def first_word(text):
    text = text.strip(" ,.")

    match = re.search(r"[a-zA-Z']+", text)

    if match:
        print(match.group(0))
        return match.group(0)
    return ""


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("hello.World") == "hello", 'Test6'

print('OK')
