def strip_nut_numeric(s: str) -> str:
    res = ''
    for c in s:
        if not c.isnumeric():
            break
        res += c
    return res


if __name__ == '__main__':
    result = {}
    with open('topic_classes.txt', encoding='utf-8') as topic_classes:
        for line in topic_classes:
            topic, *classes = line.split()
            temp = filter(lambda s: s, map(strip_nut_numeric, classes))
            result[topic] = sum(map(int, temp))
    print(result)
