def summ():
    try:
        with open('hw_5.txt', 'w+', encoding='utf-8') as f:
            num = input('Введите цифры через пробел: \n')
            f.writelines(num)
            my_num = num.split()
            print(f'Cумма чисел = {sum(map(int, my_num))}')
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода данных')


summ()
