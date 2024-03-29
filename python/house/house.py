sentence_parts = [
    "This is the horse and the hound and the horn",
    "that belonged to the farmer sowing his corn",
    "that kept the rooster that crowed in the morn",
    "that woke the priest all shaven and shorn",
    "that married the man all tattered and torn",
    "that kissed the maiden all forlorn",
    "that milked the cow with the crumpled horn",
    "that tossed the dog",
    "that worried the cat",
    "that killed the rat",
    "that ate the malt",
    "that lay in the house that Jack built."
]


def recite(start_verse, end_verse):
    if start_verse == end_verse :
        return [make_sentence(start_verse)]
    else:
        sentence_list = []
        for i in range(start_verse, end_verse+1):
            sentence_list.append(make_sentence(i))
        return sentence_list


def make_sentence(verse):

    target_parts = sentence_parts[-1 * verse:]
    first_part = target_parts[0]
    first_part = first_part.split()
    first_part[0], first_part[1] = "This", "is"
    if verse == 1 or verse == 11 :
        first_part.pop(2)
    first_sentence = " ".join(first_part)

    latter_sentence = ""
    for part in target_parts[1:]:
        latter_sentence = latter_sentence + " " + part

    return first_sentence + latter_sentence
