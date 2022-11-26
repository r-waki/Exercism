def sum_of_multiples(limit, multiples):

    sum_number_list = []

    for m in multiples:
        if m <= 0:
            continue

        i = 1
        number = m * i

        while number < limit:
            sum_number_list.append(number)
            i = i + 1
            number = m * i

    return sum(set(sum_number_list))
