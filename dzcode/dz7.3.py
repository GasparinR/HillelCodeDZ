def test_second_index(text, some_str):

    first_index = text.find(some_str)
    if first_index == -1:  # Если первого вхождения нет, возвращаем None
        return None

    second_index1 = text.find(some_str, first_index + len(some_str))
    if second_index1 == -1:  # Если второго вхождения нет, возвращаем None
        return None

    return second_index1


def second_index(text, some_str):
    result = test_second_index(text, some_str)
    print(f"second_index('{text}', '{some_str}') = {result}")
    return result  # Возвращаем результат для использования в assert


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
