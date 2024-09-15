if __name__ == '__main__':
    arr = []
    while True:
        next_el = input('Enter the next element or press Enter to finish: ')
        if next_el == '':
            break
        arr.append(next_el)

    resultArr = []
    for i in range(0, len(arr), 2):
        if i+1 < len(arr):
            resultArr.append(arr[i + 1])
        resultArr.append(arr[i])
    print(resultArr)
