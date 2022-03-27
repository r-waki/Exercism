
def score(word):

    word_list = list(word)

    one_point_set = set(list("aeioulnrstAEIOULNRST"))
    two_points_set = set(list("dgDG"))
    three_points_set = set(list("bcmpBCMP"))
    four_points_set = set(list("fhvwyFHVWY"))
    five_points_set = set(list("kK"))
    eight_points_set = set(list("jxJX"))
    ten_points_set = set(list("qzQZ"))

    one_sum = sum([1 for x in word_list if one_point_set.issuperset(x)])
    two_sum = sum([2 for x in word_list if two_points_set.issuperset(x)])
    three_sum = sum([3 for x in word_list if three_points_set.issuperset(x)])
    four_sum = sum([4 for x in word_list if four_points_set.issuperset(x)])
    five_sum = sum([5 for x in word_list if five_points_set.issuperset(x)])
    eight_sum = sum([8 for x in word_list if eight_points_set.issuperset(x)])
    ten_sum = sum([10 for x in word_list if ten_points_set.issuperset(x)])

    score = one_sum + two_sum + three_sum + four_sum + five_sum \
        + eight_sum + ten_sum

    return score
