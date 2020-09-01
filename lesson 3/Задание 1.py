# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def calculate(*numbers):
    try:
        number_1 = int(input("Ведите делимое "))
        number_2 = int(input("Введите делитель "))
        result = number_1 / number_2
    except ValueError:
        return 'Неправильный тип данных.'
    except ZeroDivisionError:
        return "Ошибка: попытка деления на 0."
    return result


print(f'Ваш результат  {calculate()}')
