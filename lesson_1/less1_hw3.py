# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input('Введите число: ')

add_1 = number + number
add_2 = number + number + number

print(f'Сумма по формуле n + nn + nnn = {int(number) + int(add_1) + int(add_2)}')