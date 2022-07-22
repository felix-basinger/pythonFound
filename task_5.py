my_list = [7, 5, 4, 3, 2]

print(f'Рейтинг - {my_list}')
print('Для выхода введите 777')
number = int(input('Введите число: '))

while number != 777:

    for i in range(len(my_list)):
        if my_list[i] == number:
            my_list.insert(i + 1, number)
            break

        elif my_list[0] < number:
            my_list.insert(0, number)
        elif my_list[-1] > number:
            my_list.append(number)
        elif my_list[i] > number > my_list[i + 1]:
            my_list.insert(i + 1, number)

    print(f'В итоге - {my_list}')
    my_list.remove(number)

    number = int(input('Введите число: '))
