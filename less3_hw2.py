# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_data(name, surname, year, city, email, mobile):
    print(f'Имя: {name}. Фамиля: {surname}. Год рождения: {year}. Город проживания: {city}. \
    Адрес электронной почты {email}. Телефон: {mobile}.')


user_name = 'Ivan'
user_surname = 'Ivanov'
user_year = '2000'
user_city = 'Moscow'
user_email = 'gmail@gmail.com'
user_mobile = '8(888)888-88-88'

user_data(name=user_name, surname=user_surname, year=user_year, city=user_city, email=user_email, mobile=user_mobile)
