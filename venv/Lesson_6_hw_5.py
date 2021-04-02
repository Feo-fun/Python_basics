class Stationery:

    def __init__(self, title='Инструмент для письма'):
        self.title = title

    def draw(self):
        print(f'{self.title}: запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'Начинаю писать с помощью ручки {self.title}.')


class Pencil(Stationery):

    def draw(self):
        print(f'Начинаю рисовать, используя карандаш {self.title}.')


class Marker(Stationery):

    def draw(self):
        print(f'Начинаю рисовать, используя маркер {self.title}.')

stationery = Stationery()
stationery.draw()

new_pen = Pen('Lamy')
new_pen.draw()

new_pencil = Pencil('Lyra PRO')
new_pencil.draw()

new_marker = Marker('BIC')
new_marker.draw()
