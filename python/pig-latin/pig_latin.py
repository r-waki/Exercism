def translate(text):
    vowel = ["a", "i", "u", "e", "o"]
    words = text.split()
    word_list = [list(x) for x in words]

    translate_word = ""

    for word in word_list:
        isConsonant = [x not in vowel for x in word]
        for consonant in isConsonant:
            if not consonant:
                break
            if word[0:2] == ["q", "u"]:
                del word[0:2]
                word.append("qu")
            elif word[0:2] == ["x", "r"]:
                break
            elif word[0:2] == ["y", "t"]:
                break
            elif word[0] == "y" and word[1] not in vowel:
                break
            else:
                word.append(word.pop(0))

        translate_word += "".join(word) + "ay "

    return translate_word.rstrip()
