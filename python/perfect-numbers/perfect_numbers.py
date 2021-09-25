def classify(number):

    if number <= 0:
        raise ValueError("number is not natural number")

    factor = [f for f in range(1, number) if number % f == 0]

    if sum(factor) == number:
        return "perfect"
    elif sum(factor) > number:
        return "abundant"
    else:
        return "deficient"
