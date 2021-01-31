"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
 """


class Matrix:
    def __init__(self, a_list):
        self.a_list = a_list

    def __str__(self):
        return "\n".join(map(str, self.a_list))

    def __add__(self, other):
        result = []
        for i in range(len(self.a_list)):
            result.append([])
            for j in range(len(self.a_list[0])):
                result[i].append(self.a_list[i][j] + other.a_list[i][j])
        return Matrix(result)


a = [[31, 22],
     [37, 43],
     [51, 86]]

b = [[43, 22],
     [1, 3],
     [44, 11]]

mtrx_1 = Matrix(a)
mtrx_2 = Matrix(b)
print(mtrx_1 + mtrx_2)
