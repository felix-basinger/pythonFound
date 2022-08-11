from random import randint
my_list = [randint(0, 20) for i in range(14)]
print(my_list)
result_list = [el for el in my_list if my_list.count(el) == 1]
print(result_list)
