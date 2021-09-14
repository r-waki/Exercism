def check_the_trianle(func):
    def inner(sides):
        if sum([a > 0 for a in sides]) != 3:
            return False

        if sides[0] + sides[1] <= sides[2]:
            return False

        if sides[0] + sides[2] <= sides[1]:
            return False

        if sides[1] + sides[2] <= sides[0]:
            return False

        return func(sides)

    return inner


@check_the_trianle
def equilateral(sides):
    return bool(len(set(sides)) == 1)


@check_the_trianle
def isosceles(sides):
    return bool(len(set(sides)) < 3)


@check_the_trianle
def scalene(sides):
    return bool(len(set(sides)) == 3)
