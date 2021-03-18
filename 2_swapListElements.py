if __name__ == '__main__':
    arr = input("Enter a string without any separators: ")
    resultArr = []
    for i in range(0, len(arr), 2):
        if i+1 < len(arr):
            resultArr.insert(i, arr[i + 1])
        resultArr.insert(i + 1, arr[i])
    print(resultArr)
