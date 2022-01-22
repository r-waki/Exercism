
def transpose(lines):
    list_length = len(lines)
    if not list_length:
        return ""

    transpose = list(lines[0])
    word_length = max([len(word) for word in lines])

    list_count = 1
    while list_count < list_length:
        word_count = 0
        word = lines[list_count]
        word_list = list(word)
        while word_count < word_length:

            if word_count < len(transpose):
                transpose[word_count] += word_list[word_count]
            else:
                transpose.append(word_list[word_count])
            word_count += 1

        list_count += 1
    
    return "\n".join(transpose)
