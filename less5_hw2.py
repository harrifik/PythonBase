# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('my_file.txt', 'r') as f:
    file_lines = f.readlines();
    print(f'Общее количество строк в файле: {len(file_lines)}.')
    for i in range(1, len(file_lines)+1):
        print(f'Количество слов в строке {i}: {len(file_lines[i-1].split())}')