from typing import Optional


def my_func(a: float, b: int) -> Optional[float]:
    if b >= 0:
        return None
    return a ** b


def my_func_list(a: float, b: int) -> Optional[float]:
    if b >= 0:
        return None
    result = 1
    for i in range(0, -b):
        result *= a
    return 1 / result


if __name__ == '__main__':
    n = float(input('Enter a number: '))
    power = int(input('Enter a negative power: '))

    res = my_func(n, power)
    print('Incorrect input') if res is None else print(res)

    res1 = my_func_list(n, power)
    print('Incorrect input') if res1 is None else print(res1)
