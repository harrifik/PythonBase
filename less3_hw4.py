# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
# в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора *.
# Второй — более сложная реализация без оператора *, предусматривающая использование цикла.


def my_func_1(x, y):
    return x**y


# не очень понятно, как обойтись без оператора *, если основание не целое?


def my_func_2(x, y):
    mul = x
    for i in range(1, abs(y)):
        mul *= x
    return 1/mul


x = 2.5
y = -4

print(my_func_1(x, y))
print(my_func_2(x, y))
