# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

my_numbers = [3, 54, 7, 0, 2, 36, 54, 3, 56, 2]
my_new_numbers = [my_numbers[i] for i in range(1, len(my_numbers)) if my_numbers[i] > my_numbers[i-1]]
print(my_new_numbers)