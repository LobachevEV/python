if __name__ == '__main__':
    monthNumber = int(input('Enter a number of a month: '))
    if monthNumber > 12:
        print('Not a month number')
    else:
        winterMonths = (12, 1, 2)
        if monthNumber in winterMonths:
            print('It is a winter month')
        else:
            springMonths = (3, 4, 5)
            if monthNumber in springMonths:
                print('It is a spring month')
            else:
                summerMonths = (6, 7, 8)
                if monthNumber in summerMonths:
                    print('It is a summer month')
                else:
                    fallMonths = (9, 10, 11)
                    if monthNumber in fallMonths:
                        print('It is a fall month')
        seasonMonthDict = {'winter': (12, 1, 2), 'spring': (3, 4, 5), 'summer': (6, 7, 8), 'fall': (9, 10, 11)}
        for season in seasonMonthDict:
            if monthNumber in seasonMonthDict[season]:
                print(f'It is a {season} month')
