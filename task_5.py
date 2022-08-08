def sum_num():
    s = 0
    while True:
        flag = False
        in_list = input('Введите число, нажмите q для выхода: ').split()
        for num in in_list:
            if num.lower() == 'q':
                return f'Cпасибо, что сыграли. Ваш результат: {s}'
            else:
                try:
                    s += int(num)
                except ValueError:
                    flag = True
        if flag:
            print('Некорректное значение')
        print(f'Cумма чисел равна: {s}')


print(sum_num())
