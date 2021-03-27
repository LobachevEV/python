from sys import argv


def calculate_salary(time_worked: float, salary_per_hour: float, reward: float) -> float:
    return time_worked * salary_per_hour + reward


if __name__ == '__main__':
    _, time_worked, salary_per_hour, reward, *_ = argv
    print(calculate_salary(float(time_worked), float(salary_per_hour), float(reward)))
