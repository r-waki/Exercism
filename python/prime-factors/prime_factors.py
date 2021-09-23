def factors(value):
    factor = []
    while value % 2 == 0:
        factor.append(2)
        value /= 2

    divisor = 3
    while divisor ** 2 <= value:
        if value % divisor == 0:
            factor.append(divisor)
            value /= divisor
        else:
            divisor += 2
    if value != 1:
        factor.append(value)

    return factor
