def personal_data(name, lastname, year, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year}'
                 f'Город проживания: {city} E-mail: {email} Телефон: {phone}')


personal_data(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year=input('Год рождения: '),
    city=input('Город проживания: '),
    email=input('E-mail:'),
    phone=input('Телефон: '),
)
