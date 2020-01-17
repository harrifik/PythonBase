# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
russian_text = []
with open('my_file.txt', 'r') as f:
    for line in f:
        if 'One' in line:
            russian_text.append(line.replace('One', 'Один'))
        if 'Two' in line:
            russian_text.append(line.replace('Two', 'Два'))
        if 'Three' in line:
            russian_text.append(line.replace('Three', 'Три'))
        if 'Four' in line:
            russian_text.append(line.replace('Four', 'Четыре'))


with open('мой_файл.txt', 'w', encoding='utf-8') as f:
    f.writelines(russian_text)
