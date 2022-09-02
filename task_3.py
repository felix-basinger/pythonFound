class Error:
    print(' ')
    print('<<<Генератор списка>>>')

    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значение списка и нажмите Enter: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n')
            except:
                print('Недопустимое значение - строка и булево')
                y_or_n = input(f'Хотите продолжить список? y/n: ')

                if y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'n':
                    return 'Удачи!'
                else:
                    return 'Удачи!'


try_except = Error(1)
print(try_except.my_input())
