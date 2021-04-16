from typing import List


class Matrix:
    def __init__(self, *rows: List[int]):
        self.__values = []
        for row in rows:
            self.__values.append(row)

    def __str__(self):
        result = ''
        for row in self.__values:
            for col in row:
                result += f'{col} '
            result += '\n'
        return result

    def __add__(self, other):
        new_matrix = []
        row_len = len(self[0])
        for i in range(0, len(self)):
            row = []
            for j in range(0, row_len):
                row.append(self[i][j] + other[i][j])
            new_matrix.append(row)
        return Matrix(*new_matrix)

    def __getitem__(self, i: int) -> List[int]:
        return self.__values[i]

    def __len__(self):
        return len(self.__values)


if __name__ == '__main__':
    m1 = Matrix([1, 2, 3, 4, 5], [9, 8, 5, 1, 2], [5, 6, 7, 4, 6])
    print('M1:')
    print(m1)
    m2 = Matrix([1, 2, 3, 4, 5], [9, 8, 5, 1, 2], [5, 6, 7, 4, 6])
    print('M2:')
    print(m2)
    print('Sum:')
    print(m1+m2)
