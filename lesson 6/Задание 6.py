# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
from time import sleep


class Stationery:
    title: str  #не понимаю, для чего этот атрибут здесь нужен, если без него всё работает

    def draw(self):
        print('Запуск отрисовки...')
        sleep(2)


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f"Инструмент для отрисовки : ручка")


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f"Инструмент для отрисовки : карандаш")


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f"Инструмент для отрисовки : маркер")


s = Pen()
s.draw()

s = Pencil()
s.draw()

s = Handle()
s.draw()

