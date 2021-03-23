if __name__ == '__main__':
    firstResult = int(input("Enter the first result in km: "))
    goal = int(input("Enter the goal in km: "))
    dayResult = firstResult
    day = 1
    dayResultStr = "{day:0g}-й день: {result:0.3g}"
    print(dayResultStr.format(day=day, result=dayResult))
    while dayResult < goal:
        dayResult *= 1.1
        day += 1
        print(dayResultStr.format(day=day, result=dayResult))
    print(day)
