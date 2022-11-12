import string


def rotate(text, key):

    rotate_text = []
    for c in text:
        if c in string.ascii_lowercase:
            rotate_charactor = shift_charactor(c, key, string.ascii_lowercase)
        elif c in string.ascii_uppercase:
            rotate_charactor = shift_charactor(c, key, string.ascii_uppercase)
        else:
            rotate_charactor = c

        rotate_text.append(rotate_charactor)

    return "".join(rotate_text)


def shift_charactor(charactor, key, alphabet_list):

    charactor_index = alphabet_list.index(charactor)
    shift_index = (charactor_index + key) % 26

    return alphabet_list[shift_index]
