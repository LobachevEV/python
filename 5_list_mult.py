from math import prod

if __name__ == '__main__':
    l = [el for el in range(100, 1001) if el % 2 == 0]
    print(l)
    print(prod(l))
