seconds = int(input('Введите секунды: '))
sec = seconds % 86400
hour = sec // 3600
sec = sec % 3600
minute = sec // 60
sec = sec % 60
print('{}:''{}:''{}'.format(hour, minute, sec))
