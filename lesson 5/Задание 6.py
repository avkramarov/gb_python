# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json
from statistics import mean

with open("Задание 6.txt", "r", encoding="UTF-8") as my_file:
    lines = [line.split() for line in my_file]
    firms = {name: int(revenue) - int(costs) for name, form, revenue, costs in lines}
    av_profit = {"average_profit": mean([value for value in firms.values() if value > 0])}
    data = [firms, av_profit]
    print(data)

with open("Задание 6.json", "w", encoding="UTF-8") as write_f:
    json.dump(data, write_f)
