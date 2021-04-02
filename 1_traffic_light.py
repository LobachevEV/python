from itertools import cycle
from time import time, sleep


class TrafficLight:
    __color_timings_s = {'red': 7, 'yellow': 2, 'green': 5}
    __color_seq_gen = (el for el in cycle(__color_timings_s.keys()))

    def __init__(self):
        self.__color = next(self.__color_seq_gen)
        self.__last_color_change_time = time()

    def running(self):
        elapsed_time = time() - self.__last_color_change_time
        delay = self.__color_timings_s[self.__color]
        if delay <= elapsed_time:
            self.__color = next(self.__color_seq_gen)
            self.__last_color_change_time = time()
        return self.__color


if __name__ == '__main__':
    traffic_light = TrafficLight()
    while True:
        print(traffic_light.running())
        sleep(1)
