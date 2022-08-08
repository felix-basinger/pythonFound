def my_func(x, y, z):
    print(f'Сумма наибольших аргументов равна: {(sum([x, y, z]) - min([x, y, z]))}')


my_func(
    int(input('Введите x: ')),
    int(input('Введите y: ')),
    int(input('Введите z: ')),
)
