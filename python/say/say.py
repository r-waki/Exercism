mapping_words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def say(number):

    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    shift_num = number

    shift_num, s1 = trans_billion(shift_num)
    shift_num, s2 = trans_million(shift_num)
    shift_num, s3 = trans_thousand(shift_num)
    shift_num, s4 = trans_handred(shift_num)
    shift_num, s5 = trans_ty(shift_num)
    return (s1 + s2 + s3 + s4 + s5).rstrip(" ")


def trans_ty(num):
    for i in range(100, 10, -10):
        digit = num // i
        if digit != 0 and num % i != 0:
            return num-i, mapping_words[i] + "-" + mapping_words[num % i] + " "
        elif digit != 0 and num % i == 0:
            return num-i, mapping_words[i] + " "
    if num % i == 0:
        return 0, ""
    return 0, mapping_words[num] + " "


def trans_handred(num):
    for i in range(1000, 0, -100):
        digit = num // i
        if digit != 0:
            return num-i, mapping_words[i/100] + " hundred" + " "
    return num, ""


def trans_thousand(num):
    for i in range(1000000, 0, -1000):
        digit = num // i
        if digit != 0:
            shift_num = i // 1000
            shift_num, s1 = trans_handred(shift_num)
            shift_num, s2 = trans_ty(shift_num)
            return num-i, s1 + s2 + "thousand" + " "
    return num, ""


def trans_million(num):
    for i in range(1000000000, 0, -1000000):
        digit = num // i
        if digit != 0:
            shift_num = i // 1000000
            shift_num, s1 = trans_handred(shift_num)
            shift_num, s2 = trans_ty(shift_num)
            return num-i, s1 + s2 + "million" + " "
    return num, ""


def trans_billion(num):
    for i in range(1000000000000, 0, -1000000000):
        digit = num // i
        if digit != 0:
            shift_num = i // 1000000000
            shift_num, s1 = trans_handred(shift_num)
            shift_num, s2 = trans_ty(shift_num)
            return num-i, s1 + s2 + "billion" + " "
    return num, ""


def trans_single_digit(num):
    return mapping_words[num]
