import random
from typing import List


def aggregate_right_bigger(l: List) -> List:
    prev_el = None
    for el in l:
        if prev_el is not None and el > prev_el:
            yield el
        prev_el = el


if __name__ == '__main__':
    init_list = random.sample(range(0, 100), 50)
    result = list(aggregate_right_bigger(init_list))
    print(init_list)
    print(result)
