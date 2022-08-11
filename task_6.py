from itertools import count

print('<<<NUM GENERATOR>>>')
el = int(input('Введите целое число, с которого начнётся отсчёт: '))
el_2 = int(input('Введите целое число, на котором отсчёт завершится: '))
for el in count(el):
    if el > el_2:
        break
    else:
        print(el)


