# Создайте собственный класс-исключение, который должен проверять содержимое списка
# на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class ErrorType(Exception):
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            val = input("Введите значения и нажимайте Enter - ")

            try:
                val = int(val)
            except ValueError:
                print(f"Вы явно вводите что-то не то. Нужно или числа или stop.")

            if type(val) is int:
                self.my_list.append(val)
            elif val == "stop":
                print(f"Завершено! Текущий список {self.my_list}")
                break


result = ErrorType(1)
print(result.my_input())
