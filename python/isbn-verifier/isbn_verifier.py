def is_valid(isbn):
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    sum_number = 0

    for index, n in enumerate(isbn[::-1]):
        if index == 0 and n == "X":
            n = 10

        try:
            sum_number += int(n) * (index + 1)
        except ValueError:
            return False

    return sum_number % 11 == 0
