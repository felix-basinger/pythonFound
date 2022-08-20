class Road:

    def __init__(self, lenght, widht):
        self._lenght = lenght
        self._widhgt = widht

    def calculate(self, weight=25, thick=5):
        return f'{self._lenght} * {self._widhgt} * {weight} * {thick} = ' \
               f'{(self._lenght * self._widhgt * weight * thick) / 1000 }'


r = Road(5000, 20)
print(r.calculate())
