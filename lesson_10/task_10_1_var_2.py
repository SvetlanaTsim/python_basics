from itertools import zip_longest

class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __iter__(self):
        return iter(self.matrix)

    def __add__(self, other):
        try:
            #zip_longest взяла для того, чтобы выдавал None в случае несоответствия матриц,
            # что провоцировало бы потом ошибку
            matrix_sum = [[cell1 + cell2 for cell1, cell2 in zip_longest(row1, row2)]
                          for row1, row2, in zip_longest(self.matrix, other)]
        except TypeError:
            return 'Эти матрицы нельзя сложить. Введите матрицы одинакового типа!'
        else:
            return str(matrix_sum)[1:-1].replace(',', '').replace('] [', '\n').replace('[', '').replace(']', '')

    def __str__(self):
        return str(self.matrix)[1:-1].replace(',', '').replace('] [', '\n').replace('[', '').replace(']', '')


mat_1 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
#print(mat_1)

mat_2 =Matrix ([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
#print(mat_2)

print(mat_1 + mat_2)
