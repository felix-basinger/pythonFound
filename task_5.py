rev = int(input('Введите размер выручки фирмы в рублях: '))
cost = int(input('Введите размер издержек фирмы в рублях: '))
pri = rev - cost
ub = cost - rev
if rev > cost:
    print(f'Прибыль фирмы равна {pri} рублей')
    print(f'Рентабельность составляет {100 * (pri / cost):.1f}%')
    workers = int(input('Введите количество сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника равна {rev / workers:.2f} рублей')
elif rev < cost:
    print(f'Убыток фирмы равен {ub} рублей')
else:
    rev = cost
    print('Выручка фирмы равна издержкам')
