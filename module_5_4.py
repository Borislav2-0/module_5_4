from random import choice, randrange


class Building:
    total = 40

    def __init__(self, total):
        self.total = total

    for i in range(total):
        i += 1
        material = choice(["солома (мазанка)", "дерево", "кирпич красный", "кирпич силикатный", "камень"])
        num_of_floors = randrange(1, 5)
        print(f'Строение № {i}, материал - {material}, количество этажей - {num_of_floors}')


building = Building(' ')
print(building)
