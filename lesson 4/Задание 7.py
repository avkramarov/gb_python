# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

def fact(n):
    step = 1
    for i in range(1, n + 1):
        step *= i
        yield step


n = int(input("Укажите факториал какого числа Вы хотели бы узнать?"))
for el in fact(n):
    print(el)
