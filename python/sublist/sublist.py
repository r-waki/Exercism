"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):

    if len(list_one) == 0 and len(list_two) != 0:
        return 1
    elif len(list_one) != 0 and len(list_two) == 0:
        return 2

    one = "".join([str(x) for x in list_one])
    two = "".join([str(x) for x in list_two])

    if one == two:
        str_one = str(sum(((x * 10 ** i) for i, x in enumerate(list_one))))
        str_two = str(sum(((x * 10 ** i) for i, x in enumerate(list_two))))
        if str_one in str_two:
            return 3
        else:
            return 4
    elif one in two:
        return 1
    elif two in one:
        return 2
    else:
        return 4
