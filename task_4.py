rus = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}
new_f = []
with open('hw_2.txt', 'r', encoding='utf-8') as f:
    for i in f:
        i = i.split(' ', 1)
        new_f.append(rus[i[0]] + ' ' + i[1])
    print(*new_f, sep='')
with open('newhw_4.txt', 'w', encoding='utf-8') as f_2:
    f_2.writelines(new_f)
