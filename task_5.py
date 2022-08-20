class Stationery:
    def __init__(self, title='Канцелярская принадлежность'):
        self.title = title

    def draw(self):
        print(f'\n{self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'\nЗапуск отрисовки ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'\nЗапуск отрисовки карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'\nЗапуск отрисовки маркером {self.title}')


s = Stationery()
pen = Pen('Pilot')
pencil = Pencil('Kores')
handle = Handle('Edding')

office_list = [s, pen, pencil, handle]

for i in office_list:
    i.draw()
