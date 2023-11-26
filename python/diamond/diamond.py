import string

def rows(letter):
    # return ["A"]
    row_length(letter)

def row_length(letter):
    letter_index = string.ascii_uppercase.index(letter)
    return 2 * letter_index + 1