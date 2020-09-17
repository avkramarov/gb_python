# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, date):

        self.date = str(date)

    @classmethod
    def extract(cls, date):
        my_date = []

        for i in date.split():
            if i != "-": my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year >= 0:
                    return f"Всё верно"
                else:
                    return f"Значение года не может быть отрицательным"
            else:
                return f"Месяцев всего 12!!!"
        else:
            return f"Ошибка"

    def __str__(self):
        return f"Текущая дата {Data.extract(self.date)}"


today = Data('11 - 1 - 2001')
print(today)


