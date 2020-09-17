# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class ZeroDivision(Exception):
    def __init__(self, dividend: int = 1, divider: int = 1):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def result(dividend, divider):
        try:
            return dividend / divider
        except:
            return f"Ошибка! Попытка деления на 0."


x = ZeroDivision()
print(x.result(100, 0))
print(x.result(10, 5))
