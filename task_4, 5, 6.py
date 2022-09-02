class OrgTechnique:
    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за штуку': self.price,
                        'Количество': self.quantity}

    def __str__(self):
        return f'{self.name}, цена: {self.price}, количество: {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование товара: ')
            unit_p = int(input('Введите цену за единицу товара: '))
            unit_q = int(input('Введите количество единиц товара: '))
            unique = {'Модель устройства': unit, 'Цена за единицу товара': unit_p, 'Количество единиц товара': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список - \n {self.my_store}')
        except:
            return 'Ошибка ввода данных'

        print('Для выхода - q\nПродолжить - Enter')
        q = input(f'--->')
        if q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад - \n {self.my_store_full}')
            return f'Выход'
        else:
            return OrgTechnique.reception(self)


class Printer(OrgTechnique):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Copier(OrgTechnique):
    def to_copier(self):
        return f'to copier smth {self.numb} times'


class Scanner(OrgTechnique):
    def to_copier(self):
        return f'to copier smth {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Copier('Xerox', 1500, 1, 15)
unit_3 = Scanner('Canon', 1200, 5, 10)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
