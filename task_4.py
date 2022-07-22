sentence = input('Введите предложение: ')

words = []
number = 1

for i in range(sentence.count(' ') + 1):
    words = sentence.split()

    if len(str(words)) <= 10:
        print(f'{number}) {words [i]}')
        number += 1

    else:
        print(f'{number}) {words[i] [0:10]}')
        number += 1
