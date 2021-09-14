def check_the_trianle(sides):

    if sum([a > 0 for a in sides]) != 3:
        return False

    if sides[0] + sides[1] <= sides[2]:
        return False

    if sides[0] + sides[2] <= sides[1]:
        return False

    if sides[1] + sides[2] <= sides[0]:
        return False

    return True


def equilateral(sides):
    if check_the_trianle(sides):
        return bool(len(set(sides)) == 1)

    return False


def isosceles(sides):
    if check_the_trianle(sides):
        return bool(len(set(sides)) < 3)

    return False


def scalene(sides):
    if check_the_trianle(sides):
        return bool(len(set(sides)) == 3)

    return False
