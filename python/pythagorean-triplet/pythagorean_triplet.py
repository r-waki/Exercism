
def triplets_with_sum(number):

    triplet = []
    for a in range(1, number):
        for b in range(a + 1, number):
            if number - a - b < b:
                break
            if a ** 2 + b ** 2 == (number - a - b) ** 2:
                triplet.append([a, b, number - a - b])

    return triplet
