class Cell:

    def __init__(self, units):
        self.units = units

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.units // rows)]) + '\n' + '*' * (self.units % rows)

    def __str__(self):
        return f'{self.units}'

    def __add__(self, other):
        print('Сумма ячеек двух клеток: ')
        return Cell(self.units + other.units)

    def __sub__(self, other):
        print('Разность ячеек двух клеток: ')
        return Cell(self.units - other.units) if self.units - other.units > 0 \
            else 'разность ячеек не может быть меньше нуля, поменяйте клетки местами!'

        # if new_cell > 0:
        #     return new_cell
        # else:
        #     return f'Результат не может быть меньше нуля!'

    def __mul__(self, other):
        print('Производное ячеек двух клеток: ')
        return Cell(self.units * other.units)

    def __truediv__(self, other):
        print('Деление ячеек двух клеток: ')
        return Cell(self.units // other.units)

cell_1 = Cell(24)
cell_2 = Cell(15)


print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)



