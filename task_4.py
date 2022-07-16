num = int(input('Введите число: '))
maximum = 0
while num > 0:
    last = num % 10
    if last > maximum:
        maximum = last
    num = num // 10
print(f'Наибольшее число: {maximum}')
