# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("Задание 4.txt", "w+", encoding="UTF-8") as my_file:
    line = input("Введите цифры через пробел >>> ")
    my_file.writelines(line)
    my_numb = line.split()
    try:
        print(sum(map(int, my_numb)))
    except ValueError:
        print("Ошибка. Неправильный тип данных")
