def translate(text):
    return " ".join(translate_word(word) for word in text.split())


def translate_word(word):
    vowel = ["a", "i", "u", "e", "o"]

    while word[0] not in vowel:
        if word[0:2] == "qu":
            word = word[2:] + word[:2]
            break
        elif word[0:2] == "xr":
            break
        elif word[0:2] == "yt":
            break
        elif word[0] == "y" and word[1] not in vowel:
            break
        else:
            word = word[1:] + word[0]

    return word + "ay"
