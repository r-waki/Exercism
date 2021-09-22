def translate(text):
    vowel = ["a", "i", "u", "e", "o"]
    text_list = list(text)

    isConsonant = [x not in vowel for x in text_list]
    for consonant in isConsonant:
        if not consonant:
            break
        if text_list[0:2] == ["q", "u"]:
            del text_list[0:2]
            text_list.append("qu")
        elif text_list[0:2] == ["x", "r"]:
            break
        elif text_list[0:2] == ["y", "t"]:
            break
        elif text_list[0] == "y" and text_list[1] not in vowel:
            break
        else:
            text_list.append(text_list.pop(0))

    return "".join(text_list) + "ay"
