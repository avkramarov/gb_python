# Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то
# новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
new_elem = int(input("Введите значение нового элемента >>>"))
for el in range(0, len(my_list)):
    if my_list[el] == new_elem:
        my_list.insert(el + 1, new_elem)
        break
    elif my_list[el] > new_elem > my_list[el + 1]:
        my_list.insert(el + 1, new_elem)
        break
    elif my_list[0] < new_elem:
        my_list.insert(0, new_elem)
    elif my_list[-1] > new_elem:
        my_list.append(new_elem)
print(my_list)
