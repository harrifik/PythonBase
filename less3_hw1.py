# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def dividend(num_1, num_2):
    if num_2 == 0:
        print('На ноль делить нельзя!')
    else:
        div = num_1 / num_2
        print(div)


number_1 = int(input('Введите делимое: '))
number_2 = int(input('Введите делитель: '))

dividend(number_1, number_2)
