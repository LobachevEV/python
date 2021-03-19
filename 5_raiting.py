from typing import List


class Rating:
    def __init__(self, initial_rating: List[int]):
        self.__items = sorted(initial_rating, reverse=True)

    def insert(self, new_val: int):
        i = 0
        while i < len(self.__items):
            if new_val > self.__items[i]:
                self.__items.insert(i, new_val)
                return
            i += 1
        self.__items.append(new_val)

    def __repr__(self):
        return ', '.join(map(str, self.__items))

    def __str__(self):
        return ', '.join(map(str, self.__items))


if __name__ == '__main__':
    rating = Rating([1, 5, 7, 8, 6, 1, 2, 5])
    print(f'Current rating: {rating}')
    entered_val = int(input('Enter a new rating: '))
    rating.insert(entered_val)
    print(rating)
