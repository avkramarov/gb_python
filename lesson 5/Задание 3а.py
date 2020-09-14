# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("Задание 3а.txt", "r", encoding="UTF-8") as my_file:
    low_salary = []
    salary = []
    my_list = my_file.read().split("\n")
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            low_salary.append(str(i[0]))
        salary.append(float(i[1]))
    avg = sum(salary) / len(salary)
    print(f"Средняя зарплата равна {round(avg, 2)}")
    print("Оклад меньше 20.000 имеют: %s." % ", ".join(low_salary))


