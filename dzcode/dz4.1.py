the_list = [0, 0, 1, 0.5, 0, -6, 0, 3, 1.1, 0.1, 9, 0]
a = [x for x in the_list if x != 0]
b = [x for x in the_list if x == 0]
result = a + b
print(result)
