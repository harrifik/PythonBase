# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.

from collections import Counter
import random

my_numbers = [random.randint(0, 100) for i in range(0, 50)]

my_new_numbers = [i for i in my_numbers if my_numbers.count(i) == 1]

# print(my_numbers)
print(my_new_numbers)
