from collections import Counter


def find_unique_value(some_list):
    count = Counter(some_list)
    for num in count:
        if count[num] == 1:
            print(num)
            return num


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
find_unique_value([2, 5, 6, 7])
print("ОК")