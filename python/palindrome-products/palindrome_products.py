import itertools


def validation_check(func):
    def inner(min_factor, max_factor):
        if min_factor > max_factor:
            raise ValueError("min_factor is larger than max_factor")
        return func(min_factor, max_factor)
    return inner


def make_palindrome_number_and_list(min_factor, max_factor):
    max_factor += 1
    factors = itertools.combinations_with_replacement(range(min_factor, max_factor), 2)
    mulitplication = [[x * y, x, y] for x, y in factors]
    palindrome_number = []
    palindrome = []

    for number in mulitplication:
        if str(number[0]) == str(number[0])[::-1]:
            palindrome_number.append(number[0])
            palindrome.append(number)

    if palindrome_number:
        min_number = min(palindrome_number)
        max_number = max(palindrome_number)
    else:
        min_number = max_number = None

    return min_number, max_number, palindrome


@validation_check
def largest(min_factor, max_factor):
    min_number, max_number, factor_list = make_palindrome_number_and_list(min_factor, max_factor)

    palindrome_factor = []
    for x in factor_list:
        if x[0] == max_number:
            palindrome_factor.append(x[1:3])

    return max_number, palindrome_factor


@validation_check
def smallest(min_factor, max_factor):
    min_number, max_number, factor_list = make_palindrome_number_and_list(min_factor, max_factor)

    palindrome_factor = []
    for x in factor_list:
        if x[0] == min_number:
            palindrome_factor.append(x[1:3])

    return min_number, palindrome_factor
