# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_str = input('Введите список, элементы которого разделены пробелом: ')
my_list = my_str.split()
print('Исходный список:', my_list)
index = 0
for i in range(int(len(my_list)/2)):
    my_list.insert(index, my_list.pop(index + 1))
    index += 2

print('Результат:', my_list)
