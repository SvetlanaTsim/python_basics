"""
Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
 что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

"""
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('car is going')

    def stop(self):
        print('car stopped')

    def turn(self, direction):
        print(f'car turned to the {direction}')

    def show_speed(self):
        print(f'speed is {self.speed}')

class TownCar(Car):
    def show_speed(self):
        print(f'speed is {self.speed}')
        if self.speed > 60:
            print('You are going over the speed limit')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f'speed is {self.speed}')
        if self.speed > 40:
            print('You are going over the speed limit')

#сделала обязательным аргумент is_police, и предупреждение, если False
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if is_police == False:
            print('Your car is not police!')

aston_martin = TownCar(120,'red','Aston Martin')
aston_martin.show_speed()
aston_martin.go()
aston_martin.stop()
aston_martin.turn('right')
print(aston_martin.name)
lada_largus = WorkCar(50,'white','Lada')
lada_largus.show_speed()
toyota_caldina = PoliceCar(60,'blue', 'Toyota Caldina', is_police=True)
print(toyota_caldina.is_police)




