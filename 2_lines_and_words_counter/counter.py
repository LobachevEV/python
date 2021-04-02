if __name__ == '__main__':
    with open('test_file.txt', 'r') as f:
        i = 0
        for line in f:
            i += 1
            print(f'Lines {i}: {len(line.strip().split())}')
        print(f'Lines number: {i}')