def division(a: float, b: float) -> float:
    if b == 0:
        return 0
    return a / b


if __name__ == '__main__':
    a, b = input('Enter a and b numbers: ').split()
    result = division(float(a), float(b))
    print(result)
