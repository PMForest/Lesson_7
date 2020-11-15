""" Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
 *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****."""


class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __str__(self):
        return f'Result of operation {self.number * "*"}'

    def __add__(self, other):
        return 'Sum of cell is ' + str(self.number + other.number)

    def __sub__(self, other):
        return self.number - other.number if self.number - other.number > 0 \
            else 'Less than or equal to, subtraction is not possible!'

    def __mul__(self, other):
        return 'Multiplication' + str(self.number * other.number)

    def __truediv__(self, other):
        return 'subdivision\n' + str(self.number / other.number)

    def make_order(self, my_numbers_row):
        row = ''
        for i in range(int(self.number / my_numbers_row)):
            row += f'{"*" * self.number}'
        row += f'{"*" * (self.number % my_numbers_row)}'
        return row

call1 = Cell(20)
call2 = Cell(10)
print(call1)
print(call1 + call2)
print(call1 - call2)
print(call1 / call2)
print(call1.make_order(15))
print(call2.make_order(30))




# Вариант препадавателя

# class Cell:
#     def __init__(self, nums):
#         self.nums = nums
#
#     def make_order(self, rows):
#         return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)
#
#     def __str__(self):
#         return str(self.nums)
#
#     def __add__(self, other):
#         return 'Sum of cell is ' + str(self.nums + other.nums)
#
#     def __sub__(self, other):
#         return self.nums - other.nums if self.nums - other.nums > 0 \
#             else 'Ячеек в первой клетке меньше или равно второй, вычитание невозможно'
#
#     def __mul__(self, other):
#         return 'Multiply of cells is ' + str(self.nums * other.nums)
#
#     def __truediv__(self, other):
#         return 'Truediv of cells is ' + str(round(self.nums / other.nums))
#
#
# cell_1 = Cell(10)
# cell_2 = Cell(34)
# print(cell_1)
# print(cell_1 + cell_2)
# print(cell_2.make_order(10))