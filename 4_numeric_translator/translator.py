if __name__ == '__main__':
    numDict = {'one': u'один', 'two': u'два', 'three': u'три', 'four': u'четыре'}
    ruLines = []
    with open('en.txt', encoding="utf-8") as en:
        for line in en:
            enStr, dash, num = line.split()
            enLower = enStr.strip().lower()
            ruLines.append(f'{numDict[enLower].capitalize()} {dash} {num.strip()}\n')
    with open('ru.txt', 'w', encoding='utf-8') as ru:
        ru.writelines(ruLines)

