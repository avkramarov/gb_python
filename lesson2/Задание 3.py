# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение через list
seasons = ["Зима", "Весна", "Осень", "Лето"]
month = int(input("Введите номер месяца "))
if month == 1 or month == 12 or month == 2:
    print(seasons[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons[1])
elif month == 9 or month == 10 or month == 11:
    print(seasons[2])
elif month == 6 or month == 7 or month == 8:
    print(seasons[3])

# Решение через dict
seasons_dict = {1: "Зима", 2: "Весна", 3: "Осень", 4: "Лето"}
month = int(input("Введите номер месяца "))
if month == 1 or month == 2 or month == 12:
    print(seasons_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(3))
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(4))
