class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.position = position
        self.surname = surname
        self.name = name
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


if __name__ == '__main__':
    position = Position('name1', 'surname1', 'position', 10000, 80000)
    print('position.name: ', position.name)
    print('position.surname: ', position.surname)
    print('position.position: ', position.position)
    print('position._income: ', position._income)
    print('position.get_full_name: ', position.get_full_name())
    print('position.get_total_income: ', position.get_total_income())
