if __name__ == '__main__':
    revenue = int(input('Enter profit: '))
    costs = int(input('Enter costs: '))
    profit = revenue - costs
    if profit < 0:
        print("Loss amount was ", -profit)
    else:
        print("Profit amount was ", profit)
        returnOfRevenue = "Return of revenue was {:3g}"
        print(returnOfRevenue.format(profit / revenue))
        employeesNumber = int(input("Enter employees number: "))
        profitPerEmployee = "Profit per employee is {:3g}"
        print(profitPerEmployee.format(profit / employeesNumber))
