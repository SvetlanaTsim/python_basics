from itertools import cycle
import time

class TrafficLight:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def color_change(self, how_many_times):
        iterator = cycle(self.__color)
        for i in range(how_many_times):
            print(next(iterator))
            time.sleep(7)
            print(next(iterator))
            time.sleep(2)
            print(next(iterator))
            time.sleep(4)

first_traf_light = TrafficLight()
first_traf_light.color_change(3)

