import itertools


def rectangles(strings):

    def vertex_list(strings):
        return [(x, y) for y, row_str in enumerate(strings) for x, e in enumerate(row_str) if e == "+"]

    def is_rectangle(vertex):
        top_left, bottom_left, top_right, bottom_right = sorted(vertex)
        return all([
          h_check(strings, top_left, top_right),
          h_check(strings, bottom_left, bottom_right),
          v_check(strings, top_left, bottom_left),
          v_check(strings, top_right, bottom_right)
        ])

    def h_check(strings, s, t):
        x1, y1 = s
        x2, y2 = t
        return y1 == y2 and x1 < x2 and all([strings[y1][i] in "+-" for i in range(x1, x2 + 1)])

    def v_check(strings, s, t):
        x1, y1 = s
        x2, y2 = t
        return x1 == x2 and y1 < y2 and all([strings[j][x1] in "+|" for j in range(y1, y2 + 1)])

    SUM = sum([1 for vt in itertools.combinations(vertex_list(strings), 4) if is_rectangle(vt)])
    return SUM
