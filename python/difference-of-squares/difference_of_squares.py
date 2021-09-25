def square_of_sum(number):
    return sum(range(1, number+1)) ** 2


def sum_of_squares(number):
    increment_list = range(1, number+1)
    return sum([num ** 2 for num in increment_list])


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
