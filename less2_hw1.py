# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['текст', 10, 3.4, complex(2, 4)]

for element in my_list:
    if isinstance(element, str):
        print(element, 'строка')
    elif isinstance(element, int):
        print(element, 'целое число')
    elif isinstance(element, float):
        print(element, 'число с плавающей точкой')
    elif isinstance(element, complex):
        print(element, 'комплексное число')
    else:
        print(element, 'тип данный не известен')