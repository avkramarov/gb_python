# Реализовать функцию my_func(), которая принимает три
# позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(number_1, number_2, number_3):

    if number_1 >= number_3 <= number_3:
        return number_1 + number_2
    elif number_2 < number_1 < number_3:
        return number_1 + number_3
    else:
        return number_2 + number_3


print(f'Результат: - {my_func(int(input("Первое число ")), int(input("Второе число ")), int(input("Третье число ")))}')
