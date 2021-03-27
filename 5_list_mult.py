from functools import reduce


if __name__ == '__main__':
    l = [el for el in range(100, 1001) if el % 2 == 0]
    print(l)
    print(reduce(lambda a, b: a*b, l))
