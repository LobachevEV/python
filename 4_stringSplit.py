if __name__ == '__main__':
    strArray = input("Enter some string: ").split(' ')
    for ind, s in enumerate(strArray, 1):
        print(f'{ind} {s[:10]}')
