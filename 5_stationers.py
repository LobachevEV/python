class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print(f'{self.title} рисует синим тонкие линии.')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print(f'{self.title} рисует черным тонкие линии.')


class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print(f'{self.title} рисует желтым жирные линии.')


if __name__ == '__main__':
    stationers = [Stationery('Канцелярская принадлежность'), Pen(), Pencil(), Handle()]
    for stationery in stationers:
        stationery.draw()
