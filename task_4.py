def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or 0 <= y:
            return 'Введите корректные значения'
        else:
            result = 1
            for i in range(abs(y)):
                result /= x
            print('Результат возведения х в степень у: ')
            return round(result, 6)
    except ValueError:
        return 'Введите числа'


num_1 = input('Введите действительное положительное число: ')
num_2 = input('Введите целое отрицательное число: ')
print(my_func(num_1, num_2))
