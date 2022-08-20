from random import choice, randit


class Car:
    """"Main Car"""
    direction = ['north', 'northeast', 'east', 'southeast',
                 'south', 'southwest,', 'west', 'northwest']

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Машина: {name}\nЦвет: {color}')

    def go(self):
        print(f'{self.name}: Машина поехала')

    def stop(self):
        print(f'{self.name}: Машина остановилась')

    def turn(self):
        print(f'{self.name}: Машина повернула {choice(self.direction)}')

    def show_speed(self):
        print(f'{self.name}: Скорость: {self.speed}')


class TownCar(Car):
    """Town Car"""

    def show_speed(self):
        return f'{self.name}: Скорость: {self.speed()}. Превышение' if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    """Truck"""

    def show_speed(self):
        return f'{self.name}: Скорость: {self.speed()}. Превышение' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """Sport"""


class PoliceCar(Car):
    """Police"""

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


town_car = TownCar(60, 'черный', 'Toyota')
work_car = WorkCar(40, 'серый', 'Jeep')
sport_car = SportCar(100, 'красный', 'Ferarri')
police_car = PoliceCar(50, 'белый', 'Lada')

list_cars = [town_car, work_car, sport_car, police_car]

for i in list_cars:
    i.go()
    i.show_speed()
    i.turn()
    i.stop()
    print()
