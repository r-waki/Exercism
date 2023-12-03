colorNumberList = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

def label(colors):
    ohms = (10 * colorNumberList[colors[0]] + colorNumberList[colors[1]]) \
         * 10 ** colorNumberList[colors[2]]

    if ohms < 1000:
        return str(ohms) + " ohms"
    elif ohms < 1000000:
        return str(int(ohms / 1000)) + " kiloohms"
    elif ohms < 1000000000:
        return str(int(ohms / 1000000)) + " megaohms"
    elif ohms < 1000000000000:
        return str(int(ohms / 1000000000)) + " gigaohms"