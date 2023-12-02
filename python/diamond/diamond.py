import string

def rows(letter):

    if letter == "A":
        return ["A"]

    # 使用されるアルファベットのリストを作成
    index = string.ascii_uppercase.index(letter)
    useLetters = string.ascii_uppercase[0:index+1]

    # CBABC のラインを作成する
    basicLine = ["A"]
    for s in useLetters[1:] :
        basicLine.insert(0, s)
        basicLine.append(s)

    # CBABC のラインに対して、A-Cから順に突合して、一致しない場合、スペースに置換
    # 前半の正三角形を作成する
    # firstHalfParts
        # '  A  ' 
        # ' B B  '
    # centerLine
        # 'C    C'

    firstHalfParts = []

    for alienChar in useLetters:
        diamondLine = []
        for checkChar in basicLine:
            if alienChar != checkChar :
                diamondLine.append(" ")
            else:
                diamondLine.append(alienChar)
        if alienChar != letter:
            firstHalfParts.append("".join(diamondLine))
        else:
            centerLine = "".join(diamondLine)

    secondHalfParts = firstHalfParts[::-1]

    # 前半と真ん中、後半をくっつけて菱形を作成する 
    diamond = []
    diamond = firstHalfParts
    diamond.append(centerLine)
    diamond.extend(secondHalfParts)

    return diamond
    