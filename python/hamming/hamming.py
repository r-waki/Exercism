def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("not match the DNA length")

    list_a = list(strand_a)
    list_b = list(strand_b)
    difference_count = 0
    for a, b in zip(list_a, list_b):
        if a != b:
            difference_count += 1

    return difference_count
