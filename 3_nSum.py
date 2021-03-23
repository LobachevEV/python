if __name__ == '__main__':
    n = int(input('Enter n: '))
    nSum = 0
    for i in range(1, 4):
        for j in range(0, i):
            nSum += n * (10 ** j)
    print(nSum)
