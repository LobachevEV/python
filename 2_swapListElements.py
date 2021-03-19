if __name__ == '__main__':
    n = int(input('Enter the number of elements: '))
    arr = []
    for i in range(0, n):
        arr.append(input('Enter the next element: '))

    resultArr = []
    for i in range(0, len(arr), 2):
        if i+1 < len(arr):
            resultArr.append(arr[i + 1])
        resultArr.append(arr[i])
    print(resultArr)
