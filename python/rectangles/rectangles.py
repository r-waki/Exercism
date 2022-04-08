import itertools


def rectangles(strings):

    # 縦線の取りうる組み合わせを特定
    row_volume = len(strings)
    vertical_combinations = itertools.combinations(range(0, row_volume), 2)

    vertex_coordinate = []

    # 任意の列の頂点となる + 座標位置を特定
    for row in strings:
        vertex_coordinate.append([i for i, e in enumerate(row) if e == "+"])

    vertical_line_element = []

    for row in strings:
        vertical_line_element.append(i for i, e in enumerate(row) if e =="+" or e == "|")


    # 縦線の組み合わせから、同じ位置に + があれば一つ長方形ができる
    square = 0
    for v in vertical_combinations:
        row_a = set(itertools.combinations(vertex_coordinate[v[0]], 2))
        row_b = set(itertools.combinations(vertex_coordinate[v[1]], 2))
 
        # vertical_line_coodinate = []

        # if v[1] - v[0] != 1 :
        #     for line_number in range( v[0]+1, v[1]+1):
        #         vertical_line_coodinate.append(itertools.combinations(vertical_line_element[line_number],2))  

        #     vertical_line = {}
        #     for i, vl in enumerate(vertical_line_coodinate):
        #         if i == 0:
        #             continue
        #         elif i == 1:
        #             vertical_line = vertical_line_coodinate[i-1] & set(vl)
        #         else:
        #             vertical_line = vertical_line & set(vl)

        #     square = square + len(row_a & row_b & vertical_line)
        # else:
        square = square + len(row_a & row_b)

    return square
