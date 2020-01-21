# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула
# (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} двигается.')

    def stop(self):
        print(f'Автомобиль {self.name} остановился.')

    def turn(self, direction):
        if direction == 'right':
            print(f'Автомобиль {self.name} повернул направо.')
        if direction == 'left':
            print(f'Автомобиль {self.name} повернул налево.')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed} км/ч.')
        if self.speed > 60:
            print(f'Вы превысили скорость на {self.speed - 60} км/ч!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed} км/ч.')
        if self.speed > 40:
            print(f'Вы превысили скорость на {self.speed - 40} км/ч!')


class PoliceCar(Car):
    pass


my_town_car = TownCar(65, 'white', 'town_car', False)
print(my_town_car.speed, my_town_car.color, my_town_car.name, my_town_car.is_police)
my_town_car.go()
my_town_car.stop()
my_town_car.turn('left')
my_town_car.show_speed()

my_sport_car = SportCar(130, 'red', 'sport_car', False)
my_sport_car.show_speed()

my_work_car = WorkCar(35, 'black', 'work_car', False)
my_work_car.show_speed()

police_car = PoliceCar(70, 'blue', 'police_car', True)
police_car.show_speed()
