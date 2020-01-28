# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data_1 = input("Введите делимое: ")
inp_data_2 = input("Введите делитель: ")

try:
    inp_data_1 = int(inp_data_1)
    inp_data_2 = int(inp_data_2)
    if inp_data_2 == 0:
        raise MyError("Нельзя делить на ноль!")
except ValueError:
    print("Вы ввели не число")
except MyError as err:
    print(err)
else:
    res = inp_data_1/inp_data_2
    print(f"Результат деления: {res}")
