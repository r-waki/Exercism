def is_armstrong_number(number):
    index = len(str(number))
    return number == sum([int(n) ** index for n in list(str(number))])
