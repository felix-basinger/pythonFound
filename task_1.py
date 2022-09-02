class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != '-': date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Right!'
                else:
                    return f'Wrong year'
            else:
                return f'Wrong month'
        else:
            return f'Wrong day'

    def __str__(self):
        return f'Current date{Date.extract(self.day_month_year)}'


today = Date('22 - 08 - 2022')
print(today)
print(Date.valid(13, 11, 2002))
print(today.valid(17, 13, 2023))
print(Date.extract('20 - 04 - 2017'))
print(today.extract('13 - 04 - 2022'))
print(Date.valid(1, 11, 2000))
