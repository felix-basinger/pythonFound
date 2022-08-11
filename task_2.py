from random import randint
my_list = [randint(1, 99) for i in range(13)]
result_list = []
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        result_list.append(my_list[i])

print(f'FIRST LIST = {my_list}\nSECOND LIST = {result_list}')
