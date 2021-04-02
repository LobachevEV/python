import random


def random_list_generator():
    l = random.randrange(100)
    for i in range(0, l):
        yield random.randrange(1000)


if __name__ == '__main__':
    with open('test.txt', 'w') as f:
        f.writelines(map(lambda a: f'{a} ', list(random_list_generator())))
    with open('test.txt') as f:
        print('Sum of numbers if the file:', sum(map(int, f.readline().split())))