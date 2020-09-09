# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle

for i in count((int(input("Введите начальное число, от 0 до 9 >>>"))), 1):
    if i > 10:
        break
    else:
        print(i)

my_list = [1, 2, 3, 4]
step = 0
for el in cycle(my_list):
    if step < 4:
        print(my_list)
        step +=1
    else:
        break
