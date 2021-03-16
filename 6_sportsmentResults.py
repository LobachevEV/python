if __name__ == '__main__':
    firstResult = int(input("Enter the first result in km: "))
    goal = int(input("Enter the goal in km: "))
    dayResult = firstResult
    day = 1
    while dayResult < goal:
        dayResult *= 1.1
        day += 1
    print(day)
