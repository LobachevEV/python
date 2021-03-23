def my_func(a, b, c):
    sorted_list = sorted([a, b, c], reverse=True)
    return sorted_list[0] + sorted_list[1]


if __name__ == '__main__':
    a = input('Enter the first number: ')
    b = input('Enter the second number: ')
    c = input('Enter the third number: ')
    print(my_func(float(a), float(b), float(c)))