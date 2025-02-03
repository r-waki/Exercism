from collections import deque

numbers_grid = [ 
     " _ | ||_|   " ,
     "     |  |   " ,
     " _  _||_    " ,
     " _  _| _|   " ,
     "   |_|  |   " ,
     " _ |_  _|   " ,
     " _ |_ |_|   " ,
     " _   |  |   " ,
     " _ |_||_|   " ,
     " _ |_| _|   " 
]


def convert(input_grid):

    check_grid_number(input_grid)
    que_grid = deque(input_grid)
    chars = ""

    while que_grid:
        first_row = que_grid.popleft()
        second_row = que_grid.popleft()
        third_row = que_grid.popleft()
        fourth_row = que_grid.popleft()

        check_columns_number(first_row)
        check_columns_number(second_row)
        check_columns_number(third_row)
        check_columns_number(fourth_row)

        char_count = int(len(input_grid[0]) / 3)

        for x in range(char_count):
            char = ""
            char += first_row[ 3*x : 3*(x+1) ]
            char += second_row[ 3*x : 3*(x+1) ]
            char += third_row[ 3*x : 3*(x+1) ]
            char += fourth_row[ 3*x : 3*(x+1) ]

            iter_numbers_grid = iter(numbers_grid)
            for i, y in enumerate(iter_numbers_grid):
                if y == char:
                    chars += str(i)
                    break
            else:
                chars += "?"
        if que_grid:
            chars += ","
    return chars

def check_grid_number(input_grid):
    if len(input_grid) % 4 == 0 :
        return True
    raise ValueError("Number of input lines is not a multiple of four")

def check_columns_number(col):
    if len(col) % 3 == 0:
        return True
    raise ValueError("Number of input columns is not a multiple of three")
