# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
# и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

summa = 0
print('Для завершения программы введите: q')
while(True):
    line = input('Введите строку чисел, разделенных пробелом: ')

    if 'q' in line.split():
        for i in range(len(line.split())):
            if i != 'q':
                summa += int(i)
            else:
                break
        print(summa)
        break

    summa += sum(list(map(int, line.split())))
    print(summa)


