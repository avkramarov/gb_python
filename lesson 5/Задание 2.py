# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

import re

with open("Задание 2.txt", "r", encoding="UTF-8") as file:
    lines_list = [re.findall(r"\w+", line) for line in file]
    lines_count = len(lines_list)
    print(f"В файле {lines_count} строк.")
    lines = 0
    for line in lines_list:
        words_count = len(line)
        lines += 1
        print(f"Количество слов в {lines}-й строке: {words_count}")

