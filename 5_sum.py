if __name__ == '__main__':
    sum = 0
    while True:
        next_els = input('Enter next elements or # to finish: ').split()
        i = 0
        for el in next_els:
            if el == '#':
                break
            sum += float(el)
        print(sum)
        if '#' in next_els:
            break
