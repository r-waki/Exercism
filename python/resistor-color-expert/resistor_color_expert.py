c_number = { "black" : 0
, "brown" : 1
, "red" : 2
, "orange" : 3
, "yellow" : 4
, "green" : 5
, "blue" : 6
, "violet" : 7
, "grey" : 8
, "white" : 9
}

def resistor_label(colors):
    if len(colors) == 4 :
        return (c_number[colors[0]] * 10 ^2 + c_number[colors[1]]* 10^1) * 10 ** c_number[colors[2]]
    elif len(colors) == 5:
        pass
    else:
        raise(Exception)

