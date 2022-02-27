"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road():
    _length: int
    _width: int

    def __init__(self, _length, _width, mass, thickness):
        self._length = _length
        self._width = _width
        self.thickness = thickness
        self.mass = mass

    def massa(self):
        return (self._length * self._width * self.mass * (self.thickness / 100)) * 0.1

m = Road(20, 5000, 25, 5)
print(f'Масса асфальта: {m.massa()} тонн')
