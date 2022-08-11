from math import factorial

print('<<<Программа вычисления факториала числа>>>')
num = int(input('Введите число: '))


def fact(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)


for el in fact(num + 1):
    print(el)
