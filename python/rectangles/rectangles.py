import itertools
import numpy as np


def rectangles(strings):

    # 縦線の取りうる組み合わせを特定
    row_volume = len(strings)
    vertical_combinations = itertools.combinations(range(0, row_volume), 2)

    # 任意の列の頂点となる + 座標位置を特定
    column_number = 0
    vertex_coordinate = []
    for row in strings:
        vertex_coordinate.append([i for i, e in enumerate(row) if e == "+"])
        column_number = len(row)

    # 縦と横を入れ替えたリストを作成する
    tr = []
    for i in range(column_number):
        tr_row = []
        for vector in strings:
            tr_row.append(vector[i])
        tr.append(tr_row)


    # 縦線の組み合わせから、同じ位置に + があれば一つ長方形ができる
    square = 0
    for v in vertical_combinations:
        row_a = set(itertools.combinations(vertex_coordinate[v[0]], 2))
        row_b = set(itertools.combinations(vertex_coordinate[v[1]], 2))

        ab = (row_a & row_b)

        if v[1] - v[0] > 1:

            for x in list(ab):
                column_a = "".join(tr[x[0]])
                column_b = "".join(tr[x[1]])
                if all((y == "|" or y == "+") for y in column_a[v[0]+1:v[1]]) and\
                   all((y == "|" or y == "+") for y in column_b[v[0]+1:v[1]]):
                    square = square + 1
        else:
            square = square + len(ab)

    return square
