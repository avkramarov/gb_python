# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

class Textil:
    def __init__(self, v=1, h=1):
        self.v = v
        self.h = h

    def get_square_c(self):
        return self.v / 6.5 + 0.5

    def get_square_j(self):
        return self.h * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f"Общий расход ткани {round(((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)), 2)} м2")

class Coat(Textil):
    def __init__(self, v):
        super().__init__(v)
        self.square_c = round((self.v / 6.5 + 0.5), 2)

    def __str__(self):
        return f"Необходимо ткани на пальто {self.square_c} м2"


class Jacket(Textil):
    def __init__(self, h):
        super().__init__(h)
        self.square_j = round((self.h * 2 + 0.3), 2)

    def __str__(self):
        return f"Необходимо ткани  на костюм {self.square_j} м2"


coat = Coat(2)
jacket = Jacket(1)
print(coat)
print(jacket)
print(coat.get_sq_full)

