"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

my_list = []
while True:
    data = input('Введите данные: ')
    if data == '':
        exit()
    else:
        line = data + '\n'
        my_list.append(line)

    with open('test.txt', 'w') as file_obj:
        file_obj.writelines(my_list)

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_list = ['words are spoken to\n', 'be broken\n', 'feelings are intense words are trivial\n']
with open('test1.txt', 'w') as file_obj:
    file_obj.writelines(my_list)

with open('test1.txt') as file_obj:
    lines = 0
    for line in file_obj:
        lines += 1
        marker = 0
        word = 0
        for i in line:
            if i != ' ' and marker == 0:
                word += 1
                marker = 1
            elif i == ' ':
                marker = 0
        print(line, len(line), 'символов', word, 'слов')

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""

from statistics import mean

with open('workers.txt', 'r') as input:
    workers = {}
    salaries = []
    for line in input:
        key, value = line.split()
        workers[key] = value
        salary = int(value)
        salaries.append(salary)
        if int(value) < 20000:
            print(f'{key}: зарплата меньше 20000')
    print(mean(salaries))

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('numbers.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)

with open('numbers.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

try:
    with open('file_5.txt', 'w+') as file_obj:
        line = input('Введите цифры через пробел \n')
        file_obj.writelines(line)
        my_numb = line.split()
        print(sum(map(int, my_numb)))

except ValueError:
    print('Ошибка ввода-вывода')


"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
subjects = {}
with open('file_6.txt', 'r') as file_obj:
    for line in file_obj:
        subject, lecture, practice, lab = line.split()
        subjects[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subjects}')

"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,

а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь 
(со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')