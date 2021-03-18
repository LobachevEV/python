if __name__ == '__main__':
    arr = [2, 2.5, 2 + 4j, 'some string', [1, 2, 3], (1, 2, 3), True, b'some string', bytearray(b'some string')]
    for el in arr:
        print(type(el))
