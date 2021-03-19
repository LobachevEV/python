from typing import List


class Rating:
    def __init__(self, initial_rating: List[int]):
        self.__initialRating = sorted(initial_rating, reverse=True)

    def insert(self, new_element: int):
        i = 0
        while i < len(self.__initialRating):
            if new_element > self.__initialRating[i]:
                self.__initialRating.insert(i, new_element)
                return
            i += 1
        self.__initialRating.append(new_element)

    def __repr__(self):
        return ', '.join(map(str, self.__initialRating))

    def __str__(self):
        return ', '.join(map(str, self.__initialRating))


if __name__ == '__main__':
    rating = Rating([1, 5, 7, 8, 6, 1, 2, 5])
    print(f'Current rating: {rating}')
    newEl = int(input('Enter a new rating: '))
    rating.insert(newEl)
    print(rating)
