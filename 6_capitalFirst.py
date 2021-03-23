def int_func(s:str)->str:
    return s.capitalize()


if __name__ == '__main__':
    input_str = input('Enter a string: ').split()
    print(' '.join(map(int_func, input_str)))

