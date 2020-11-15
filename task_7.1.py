""" Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
          класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д."""

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        mat =[[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

        for i in range(len(self.list_1)):

            for x in range(len(self.list_2[i])):
                mat[i][x] = self.list_1[i][x] + self.list_2[i][x]

        return str('\n'.join(' '.join([str(x) for x in i]) for i in mat))

    def __str__(self):
        mat = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

        return str('\n'.join(' '.join([str(x) for x in i]) for i in mat))

new_matrix = Matrix([[3, 5, 32],
                   [2, 4, 6],
                   [-1, 64, -8]],
                    [[31, 10, 22],
                     [37, 20, 43],
                     [51, -10, 86]])

print(new_matrix.__add__())


# вар 2

class Matrix_2:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        mat =[[0, 0],
              [0, 0],
              [0, 0]]

        for i in range(len(self.list_1)):

            for x in range(len(self.list_2[i])):
                mat[i][x] = self.list_1[i][x] + self.list_2[i][x]

        return str('\n'.join(' '.join([str(x) for x in i]) for i in mat))

    def __str__(self):
        mat = [[0, 0],
               [0, 0],
               [0, 0]]

        return str('\n'.join(' '.join([str(x) for x in i]) for i in mat))

new_matrix = Matrix_2([[3, 5],
                   [2, 4],
                   [-1, 64]],
                    [[31, 10],
                     [37, 20],
                     [51, -10]])

print(new_matrix.__add__())


# Вариант препадователя

class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Problems with shape'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in summed_line]) + '\n'
        else:
            return 'Problems with shape'
        return answer


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])

print(matrix_1)
print()
print(matrix_1 + matrix_2)  # matrix_1.__add__(matrix_2)