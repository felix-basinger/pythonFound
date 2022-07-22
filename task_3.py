month = int(input('Введите номер месяца: '))

season_list = ['Winter', 'Spring', 'Summer', 'Autumn']
season_dict = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'}

if month == 12 or month == 1 or month == 2:
    print(season_list[0])
    print(season_dict.get(1))

elif month == 3 or month == 4 or month == 5:
    print(season_list[1])
    print(season_dict.get(2))

elif month == 6 or month == 7 or month == 8:
    print(season_list[2])
    print(season_dict.get(3))

elif month == 9 or month == 10 or month == 11:
    print(season_list[3])
    print(season_dict.get(4))

else:
    print('Такого месяца еще не придумали')
