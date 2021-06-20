'''
Создать класс TrafficLight (светофор):
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться
только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
from itertools import cycle
import time

class TrafficLight:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def color_change(self, how_many_times):
        count = 1
        for color in cycle(self.__color):
            if count > how_many_times:
                break
            else:
                if color == 'red':
                    print(color)
                    time.sleep(7)
                elif color == 'yellow':
                    print(color)
                    time.sleep(2)
                elif color == 'green':
                    print(color)
                    time.sleep(4)
                    count+=1

first_traf_light = TrafficLight()
first_traf_light.color_change(3)






