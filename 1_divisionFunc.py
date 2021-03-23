from typing import Optional


def division(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b


if __name__ == '__main__':
    a, b = input('Enter a and b numbers: ').split()
    result = division(float(a), float(b))
    print(result)
