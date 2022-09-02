class DivisionByNull:

    def __init__(self, div, den):
        self.divider = div
        self.denominator = den

    @staticmethod
    def divide_by_null(div, den):
        try:
            return div / den
        except:
            return 'На ноль не делится'


divider = int(input('Введите делимое: '))
denominator = int(input('Введите делитель: '))
div_1 = DivisionByNull
print(div_1.divide_by_null(divider, denominator))
