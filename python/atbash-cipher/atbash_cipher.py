import string

plain_alphabet = string.ascii_lowercase
encode_alphabet = plain_alphabet[::-1]
digits = string.digits
plain_alphabet = plain_alphabet + digits
encode_alphabet = encode_alphabet + digits


def encode(plain_text):

    encode_words = [encode_alphabet[plain_alphabet.index(word)] for word in plain_text.lower() if word in plain_alphabet]
    encode_words = "".join(encode_words)

    encode_text = encode_words[0:5]

    for i in range(5, len(encode_words), 5):
        fixed_five_len = encode_words[i:i+5]
        encode_text = encode_text + " " + fixed_five_len

    return "".join(encode_text)


def decode(ciphered_text):
    plain_text = [plain_alphabet[encode_alphabet.index(word)] for word in ciphered_text.lower() if word in encode_alphabet]
    return "".join(plain_text)
