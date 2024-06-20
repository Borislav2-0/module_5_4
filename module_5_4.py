from random import choice


class Building:
    total = 40

    def __init__(self, total):
        self.total = total

    for i in range(total):
        i += 1
        material = choice(["солома (мазанка)", "дерево", "кирпич красный", "кирпич силикатный", "камень"])
        print(f'Строение № {i}, материал - {material}')


building = Building(' ')
print(building)
