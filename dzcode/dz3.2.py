lst = [1, 2, 3, 4, 5]  # даем переменной тип листа
if 1 in lst:  # проверяем наличие хотя бы 1 индекса, что бы потом последнюю цифру перенести в начало
    lst_last_id = lst.pop()  # забираем у листа последний ID с помощью pop()
    lst.insert(0, lst_last_id)  # добавляем в наш лист последнюю цифру которую мы забирали ранее
    print(lst)
else:
    print(lst)
