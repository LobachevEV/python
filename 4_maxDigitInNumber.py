if __name__ == '__main__':
    number = int(input('Enter the number: '))
    divisionResult = -1
    power = 1
    digits = []
    while divisionResult != 0:
        tenInPower = 10 ** power
        divisionResult = int(number / tenInPower)
        digit = int(number % tenInPower / (10 ** (power - 1)))
        digits.append(digit)
        power += 1
    maxDigit = 0
    for i in digits:
        if i > maxDigit:
            maxDigit = i

    print(maxDigit)
