# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, string):
        self.string = string

    @classmethod
    def digit(cls, string):
        print(list(map(int, string.split('-'))))

    @staticmethod
    def valid(string):
        day, month, year = list(map(int, string.split('-')))
        print('День задан корректно.') if 0 < day <= 31 else print('День задан не корректно.')
        print('Месяц задан корректно.') if 0 < month <= 12 else print('Месяц задан не корректно.')


Data.digit('28-01-2020')
Data.valid('28-01-2020')
Data.valid('28-14-2020')
