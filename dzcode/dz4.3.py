import random
# Создание списка случайной длины от 3 до 10:
initial_list = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
# Создание нового списка с первым, третьим и вторым с конца элементами:
new_list = [initial_list[0], initial_list[2], initial_list[-2]]
print("Начальный список:", initial_list)  # Вывод начального и нового списка
print("Новый список:", new_list)
