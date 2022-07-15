seconds = int(input('Введите секунды: '))
sec = seconds % 86400
hour = sec // 3600
sec = sec % 3600
minutes = sec // 60
sec = sec % 60
print('{} ч : ''{} м : ''{} с'.format(hour, minutes, sec))
