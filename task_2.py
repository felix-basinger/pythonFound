with open('hw_2.txt', 'r', encoding='utf-8') as f:
    my_f = f.readlines()
    for count, value in enumerate(my_f, start=1):
        num = len(value.split())
        print(f'В {count} строке - {num} слов')
    print(f'Всего строк {len(my_f)}')
