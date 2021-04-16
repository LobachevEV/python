from __future__ import annotations


class Cell:
    def __init__(self, units: int):
        if units < 0:
            raise Exception('Units number cannot be less then 0')
        self.units = units

    def __add__(self, other) -> Cell:
        return Cell(self.units + other.units)

    def __sub__(self, other) -> Cell:
        if self.units < other.units:
            raise Exception('Diff is less then 0')
        return Cell(self.units - other.units)

    def __mul__(self, other) -> Cell:
        return Cell(self.units * other.units)

    def __truediv__(self, other) -> Cell:
        return Cell(self.units // other.units)

    def __str__(self) -> str:
        return f'{self.units}'

    def make_order(self, units_in_row: int) -> str:
        if units_in_row < 0:
            raise Exception('There cannot be less then 0 units in a row')
        i = 0
        result = ''
        units_left = self.units
        while i < self.units:
            result += ('*' * units_in_row + '\\n' if units_left > units_in_row else '*' * units_left)
            i += units_in_row
            units_left -= units_in_row
        return result


if __name__ == '__main__':
    cell_1 = Cell(10)
    cell_2 = Cell(57)
    print('cell_2 + cell_1 = ', cell_2 + cell_1)
    print('cell_2 - cell_1 = ', cell_2 - cell_1)
    try:
        print('cell_1 - cell_2 = ', cell_1 - cell_2)
    except Exception as ex:
        print('cell_1 - cell_2 = ', ex)
    print('cell_2 * cell_1 = ', cell_2 * cell_1)
    print('cell_2 / cell_1 = ', cell_2 / cell_1)
    print('cell_1.make_order(3)')
    print(cell_1.make_order(3))
    print('cell_2.make_order(5)')
    print(cell_2.make_order(5))
