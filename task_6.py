start = int(input('Введите результат первого дня (в километрах): '))
finish = int(input('Введите желаемый результат (в километрах): '))
day = 1
while start < finish:
    start += start * 0.1
    day += 1
print(f'Вы достигните результата {finish} километров за {day} дней!')
