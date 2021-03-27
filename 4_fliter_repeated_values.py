import random
from typing import List, Iterable


def repeat_values(l: Iterable, count=0):
    i = 0
    while count != 0 and count > i:
        i += 1
        yield random.choice(l)


def filter_repeated_values(l: List) -> List:
    copy_l = l.copy()
    for el in l:
        copy_l.remove(el)
        if el not in copy_l:
            yield el
        copy_l.append(el)


if __name__ == '__main__':
    init_list = list(repeat_values(range(0, 10), 10))
    result = list(filter_repeated_values(init_list))
    print(init_list)
    print(result)
