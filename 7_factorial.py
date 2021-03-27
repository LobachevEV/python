from math import prod


def my_factorial(n: int):
    for i in range(1, n+1):
        yield prod(range(1, i + 1))


if __name__ == '__main__':
    for el in my_factorial(4):
        print(el)
