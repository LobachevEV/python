from itertools import count, cycle
from typing import Iterable


def integers_generator(start: int, end: int):
    for el in count(start):
        if el >= end:
            break
        else:
            yield el


def repeater(seq: Iterable, count: int):
    i = 0
    for el in cycle(seq):
        if i >= count:
            break
        else:
            i += 1
            yield el
