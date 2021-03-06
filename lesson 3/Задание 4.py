# Программа принимает действительное положительное число x
# и целое отрицательное число y. Необходимо выполнить возведение
# числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Вариант 1: возведение в степень с помощью оператора **.

def my_func(x, y):
    return x ** y


print(f'Результат: - {my_func(int(input("Первое число ")), int(input("Второе число ")))}')


# Вариант 2: с помощью цикла

def my_func(x, y):
    if y < 0:
        result = (1 / x) * (1 / x)
        while y < -2:
            result = result * (1 / x)
            y += 1
        return result
    else:
        return "ошибка"


print(f'Результат: - {my_func(int(input("Первое число ")), int(input("Второе число ")))}')
