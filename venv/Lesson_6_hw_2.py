class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self):
        return f'{self._length} * {self._width} * 25 м * 5 см = {(self._length * self._width * 25 * 5) / 1000} тонн'

new_road = Road(5000, 20)

print(new_road.get_mass())
