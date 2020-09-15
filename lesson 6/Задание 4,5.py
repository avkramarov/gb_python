# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# 5. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
from time import sleep


class Car:
    speed: float
    name: str
    color: str
    is_police: bool

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.is_police = False
        self.speed = 0
        sleep(2)

    def go(self, speed):
        self.speed = speed
        print(f"{self.color} {self.name} поехала")

    def stop(self, speed):
        self.speed = speed
        print(f"{self.color} {self.name} остановилась")

    def turn(self, direction: str):
        value = ("налево", "направо")
        print(f"{self.color} {self.name} повернула {direction}")

    def show_speed(self):
        print(f"{self.color} {self.name} движется со скоростю {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)


    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.color} {self.name} - превышение скорости")


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)



class WorkCar(Car):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.color} {self.name} - превышение скорости")


class PoliceCar(Car):
    def __init__(self, name, color, is_police: bool = True):
        super().__init__(name, color)
        self.name = "полицейская " + self.name


x = TownCar("Мазда", "серая")
x.go(70)
x.show_speed()
x.turn("налево")
x.stop(0)
x.go(20)
x.show_speed()
x.turn("направо")


x = SportCar("Ламборджини", "красная")
x.go(70)
x.show_speed()
x.turn("налево")
x.stop(0)
x.go(20)
x.show_speed()
x.turn("направо")


x = WorkCar("Газель", "грязная")
x.go(70)
x.show_speed()
x.turn("налево")
x.stop(0)
x.go(20)
x.show_speed()
x.turn("направо")


x = PoliceCar("BMW", "синяя с мигалкой")
x.go(70)
x.show_speed()
x.turn("налево")
x.stop(0)
x.go(20)
x.show_speed()
x.turn("направо")
