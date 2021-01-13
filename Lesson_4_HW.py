"""
    1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
    В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv
name, work_hours, bonus, sal = argv

salary = int(work_hours) * int(work_hours) + int(bonus)
print(f'Your salary is {salary}')

"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
 значения которых больше предыдущего элемента.
 Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
 Для формирования списка использовать генератор.
 Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
 Результат: [12, 44, 4, 10, 78, 123].
"""

old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [old_list[i] for i in range(1,len(old_list)) if old_list[i-1] < old_list[i]]

print(new_list)

"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""

numbers = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(numbers)

"""
 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
 Сформировать итоговый массив чисел, соответствующих требованию.
 Элементы вывести в порядке их следования в исходном списке.
 Для выполнения задания обязательно использовать генератор.
 Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
 Результат: [23, 1, 3, 10, 4, 11]
 """

old_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in old_list if old_list.count(i) == 1]
print(new_list)

""" 
 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
 В список должны войти четные числа от 100 до 1000 (включая границы).
 Необходимо получить результат вычисления произведения всех элементов списка.
 Подсказка: использовать функцию reduce().
"""

from functools import reduce

the_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce((lambda x,y: x * y), the_list))

""" 
 6. Реализовать два небольших скрипта:
 а) итератор, генерирующий целые числа, начиная с указанного,
 б) итератор, повторяющий элементы некоторого списка, определенного заранее.
 Подсказка: использовать функцию count() и cycle() модуля itertools.
 Обратите внимание, что создаваемый цикл не должен быть бесконечным.
 Необходимо предусмотреть условие его завершения.
 Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
 Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

n = int(input('Type the first number: '))
end = 0
for i in count(n):
    end += 1
    if end == 11:
        break
    else:
        print(i)

the_list = ['любит', 'не любит', 'плюнет', 'поцелует', 'к сердцу прижмет']
iter = cycle(the_list)
for i in range(len(the_list)):
    print(next(iter))

""" 
 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
 При вызове функции должен создаваться объект-генератор.
 Функция должна вызываться следующим образом: for el in fact(n).
 Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
 начиная с 1! и до n!.
 Подсказка: факториал числа n — произведение чисел от 1 до n.
 Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""

from math import factorial

def fact(max_num):
    for i in range(1, max_num + 1):
        yield factorial(i)

for el in fact(3):
    print(el)