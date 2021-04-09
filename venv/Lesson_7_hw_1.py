# --------------- Задание 1 ------------------------

class Matrix:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([str(itm) for itm in line]) for line in self.data)

    def __add__(self, other):
        m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
             for line in range(len(self.data))]
        return Matrix(m)

a = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
b = [[18, 41, 7], [22, 15, -31], [12, -71, 29]]

matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
new_matrix = matrix_1 + matrix_2

print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_1 + matrix_2)
print()
print(new_matrix)

