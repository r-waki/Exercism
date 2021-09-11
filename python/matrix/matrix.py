class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.splitlines()

    def row(self, index):
        string_row = self.matrix_string[index-1].split()
        row = [int(x) for x in string_row]
        return row

    def column(self, index):
        string_column = [y.split() for y in self.matrix_string]
        column = [int(y[index-1]) for y in string_column]
        return column
