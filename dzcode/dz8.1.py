def add_one(some_list):

    number = int(''.join(map(str, some_list)))

    number += 1

    result = [int(digit) for digit in str(number)]
    print(result)  # Выводим результат
    return result


assert add_one([1, 2, 3, 4])
assert add_one([9, 9, 9])
assert add_one([0])
assert add_one([9])
print("ОК")
