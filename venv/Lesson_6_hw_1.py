# ____________________Задание 1______________________

from time import sleep

class TrafficLight:
    __color = 'color'

    def running(self):
        while True:
            print('Красный свет - дороги нет!')
            sleep(7)
            print('Жёлтый - будь готов к пути!')
            sleep(2)
            print('А зелёный свет - кати!')
            sleep(10)
            print('Снова жёлтый - тормози!')
            sleep(2)

trafficlight = TrafficLight()
trafficlight.running()


