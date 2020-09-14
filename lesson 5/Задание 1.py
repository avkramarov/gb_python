# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

lines = []
new_item = input("Введите значение >>>")
while new_item != "":
    lines.append(new_item)
    new_item = input("Введите значение >>>")

with open(r"Задание 1.txt", "w") as my_file:
    for line in lines:
        my_file.write(line + '\n')
