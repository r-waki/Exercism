def abbreviate(words):
    words = words.replace('-', ' ')
    words = words.replace('_', ' ')
    words = words.upper()
    words_list = words.split()

    initial_list = [word[0] for word in words_list]
    return ''.join(initial_list)
