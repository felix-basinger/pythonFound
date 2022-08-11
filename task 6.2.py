from itertools import cycle
from random import randint

gen = 1
print('<<<ИТЕРАТОР, ПОВТОРЯЮЩИЙ ЭЛЕМЕНТЫ СПИСКА>>>')
print('Создайте свой уникальный список чисел')
el_1 = int(input('Введите  наименьшее целое число: '))
el_2 = int(input('Введите наибольшее целое число: '))
el_3 = int(input('Введите количество элементов в списке: '))
my_list = [randint(el_1, el_2) for i in range(el_3)]
itr = cycle(my_list)
print(f'Ваш список: {my_list}')
print('VVV Ваши элементы списка VVV')
for i in cycle(my_list):
    if gen > el_3:
        break
    print(i)
    gen += 1
