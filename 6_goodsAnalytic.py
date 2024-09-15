from typing import Tuple, List

indexed_product = Tuple[int, dict]


class Goods:
    def __init__(self):
        self.__items: List[indexed_product] = []

    def add(self, name: str, price: int, amount: float, units: str):
        next_idx = len(self.__items) + 1
        self.__items.append((next_idx, {'name': name, 'price': price, 'amount': amount, 'units': units}))

    def analytic(self) -> dict:
        result = {'name': [], 'price': [], 'amount': [], 'units': []}
        for idx, product in list(self.__items):
            for key in result:
                new_val = product[key]
                if new_val not in result[key]:
                    result[key].append(product[key])
        return result

    def __repr__(self):
        return '\n'.join(map(str, self.__items))

    def __str__(self):
        return '\n'.join(map(str, self.__items))


if __name__ == '__main__':
    print('Product format: name price amount units. All fields separated by space.')
    goods = Goods()
    while True:
        productStr = input('Enter a new product or press Enter to finish: ')
        if productStr == '':
            break
        product = productStr.split(' ')
        if len(product) < 4:
            print("Incorrect input format")
            continue
        name, price, amount, units, *_ = productStr.split(' ')
        goods.add(name, int(price), float(amount), units)
    print(goods)
    analytic = goods.analytic()
    for title in analytic:
        print(f'{title}: {analytic[title]}')

