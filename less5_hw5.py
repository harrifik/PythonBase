# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

numbers = '1 2 4 7 6 4 7'

with open('my_file.txt', 'r+') as f:
    f.write(numbers)
    summa = 0
    for i in range(len(numbers.split())):
        summa += int(numbers.split()[i])
    print(summa)


