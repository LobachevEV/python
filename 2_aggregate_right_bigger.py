import random
from typing import Iterable, List


def aggregate_right_bigger(l: List) -> List:
    length = len(l)
    for i in range(0, length):
        if i + 1 >= length:
            return
        if l[i + 1] > l[i]:
            yield l[i+ 1]


if __name__ == '__main__':
    init_list = random.sample(range(0, 100), 50)
    result = list(aggregate_right_bigger(init_list))
    print(init_list)
    print(result)
