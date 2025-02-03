
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

    first_row = input_grid[0]
    second_row = input_grid[1]
    third_row = input_grid[2]
    fourth_row = input_grid[3]

    check_grid_number(input_grid)
    check_columns_number(first_row)
    check_columns_number(second_row)
    check_columns_number(third_row)
    check_columns_number(fourth_row)

    char_count = int(len(input_grid[0]) / 3)
    chars = ""

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
    return chars

def check_grid_number(input_grid):
    if len(input_grid) % 4 == 0 :
        return True
    raise ValueError("Number of input lines is not a multiple of four")

def check_columns_number(col):
    if len(col) % 3 == 0:
        return True
    raise ValueError("Number of input columns is not a multiple of three")
