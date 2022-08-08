def div(x, y):
    try:
        return x / y
    except ZeroDivisionError as err:
        return err


print(div(int(input('Введите первое число: ')), int(input('Введите первое число: '))))
