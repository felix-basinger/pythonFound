with open('hw_3.txt', 'r', encoding='utf-8') as f:
    sal = []
    low = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            low.append(i[0])
        sal.append(i[1])
print(f'Средний оклад = {sum(map(float, sal)) / len(sal)} \nОклад меньше 20000:', *low, sep='\n')
