if __name__ == '__main__':
    with open('employee_salary.txt') as f:
        salarySum = 0
        employeeCount = 0
        for line in f:
            employee, salaryStr = line.split()
            salary = int(salaryStr)
            if salary < 20000:
                print(employee)
            salarySum += salary
            employeeCount += 1
        print(f'Average salary: {salarySum/employeeCount}')
