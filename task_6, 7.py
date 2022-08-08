def int_func():
    for word in input("Введите слова из маленьких латинских букв:  ").split():
        syms = 0
        for sym in word:
            if 97 <= ord(sym) <= 122:
                syms += 1
        print(word.title() if syms == len(word) else '!!!ИЗ МАЛЕНЬКИХ ЛАТИНСКИХ БУКВ!!!')


int_func()
