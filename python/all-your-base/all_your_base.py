def rebase(input_base, digits, output_base):

    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if any([x < 0 or input_base <= x for x in digits]):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if not digits or sum(digits) == 0:
        return [0]

    real_number = 0

    for i, x in enumerate(digits[::-1]):
        real_number = real_number + x * input_base ** i

    shift_number = real_number
    out_digits = []

    while shift_number != 0:
        out_digits.insert(0, shift_number % output_base)
        shift_number = shift_number // output_base

    return out_digits
