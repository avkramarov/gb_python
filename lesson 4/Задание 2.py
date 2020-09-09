# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.

import random

my_list = [x for x in range(0, 100)]
new_list = random.sample(my_list, 10)
result = [el for num, el in enumerate(new_list) if new_list[num - 1] < new_list[num]]
print(new_list)
print(result)
