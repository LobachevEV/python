import random


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The car {self.name} has gone')

    def stop(self):
        print(f'The car {self.name} has stopped')

    def turn(self, direction):
        print(f'The car {self.name} has turned {direction}')

    def show_speed(self):
        print(f'{self.speed} km/h')


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f'The car {self.name} speed is too high')
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'The {self.name} car speed is too high')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    directions = ['left', 'right']
    colors = ['white', 'black', 'red', 'green', 'blue', 'yellow', 'orange', 'pink', 'marine', 'cyan', 'magenta']
    cars = [Car(50, random.choice(colors), 'Just', False), TownCar(50, random.choice(colors), 'Slow Town'),
            TownCar(70, random.choice(colors), 'Fast Town Car'), SportCar(120, random.choice(colors), 'Sport'),
            WorkCar(30, random.choice(colors), 'Slow Work'), WorkCar(50, random.choice(colors), 'Fast Work'),
            PoliceCar(50, random.choice(colors), 'Police')]
    for car in cars:
        print('type: ', type(car))
        print('car.speed:', car.speed)
        print('car.color:', car.color)
        print('car.name:', car.name)
        print('car.is_police:', car.is_police)
        car.go()
        car.stop()
        car.turn(random.choice(directions))
        car.show_speed()
