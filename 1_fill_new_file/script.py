if __name__ == '__main__':
    f = open('test_file.txt', 'w')
    s = input('Enter some text or empty string to finish: ')
    while s != '':
        f.writelines(s)
        s = input('Enter some text or empty string to finish: ')
    f.close()