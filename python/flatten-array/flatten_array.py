def flatten(iterable, outlist=None):

    if outlist is None:
        outlist = []

    for x in iterable:
        if x is None:
            continue
        elif type(x) is int:
            outlist.append(x)
        else:
            outlist = flatten(x, outlist)

    return outlist
