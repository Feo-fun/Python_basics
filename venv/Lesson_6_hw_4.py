class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Машина - {name}, цвет - {color}, скорость - {speed}, полицейская - {is_police}')

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась.')

    def turn(self, direction=False):
        print(f'Машина {self.name} повернула {"налево" if direction is not False else "направо"}')

    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed}'

class TownCar(Car):
    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed} км/час. Притормозите, вы превысили скорость!'\
            if self.speed > 60 else f'Скорость автомобиля {self.name} - {self.speed} км/час.'

class SportCar(Car):
    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed} км/час. Вррруууум вруууум!' \
            if self.speed > 120 else f'Скорость автомобиля {self.name} - {self.speed} км/час.'

class WorkCar(Car):
    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed} км/час. Притормозите, вы превысили скорость!' \
            if self.speed > 40 else f'Скорость автомобиля {self.name} - {self.speed} км/час.'

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def get_sirene(self, car_accident=False):
        print(f'Включаю сирену!!' if car_accident is not False else f'Сирена отключена.')

town_car = TownCar(50, 'Silver', 'Prius')
town_car.go()
print(town_car.show_speed())
town_car.turn(True)
town_car.stop()
print('-------')

sport_car = SportCar(140, 'Red', 'Ferrari')
sport_car.go()
print(sport_car.show_speed())
sport_car.turn(False)
sport_car.stop()
print('-------')

work_car = WorkCar(44, 'Blue', 'GMC')
work_car.go()
print(work_car.show_speed())
work_car.turn(True)
work_car.stop()
print('-------')

police_car = PoliceCar(146, 'Black', 'Ford', True)
police_car.go()
print(police_car.show_speed())
police_car.turn(True)
police_car.get_sirene(True)
police_car.stop()
print('-------')