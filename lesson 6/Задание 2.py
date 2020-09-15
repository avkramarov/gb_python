# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.

class Road:
    _length: int
    _width: int

    def __init__(self, _length, _width, _thickness: int = 5, _cost: int = 25):
        self._length = _length
        self._width = _width
        self._thickness = _thickness
        self._cost = _cost

    def total_mass(self):
        mass = self._length * self._width * self._thickness * self._cost
        print(f"Неоходимо асфальта: {mass} кг.")


x = Road(20, 5000)
x.total_mass()
