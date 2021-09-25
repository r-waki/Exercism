
def check_samechar_count(word, candidate):
    for x in set(word + candidate):
        if word.count(x) != candidate.count(x):
            return False
    return True


def find_anagrams(word, candidates):
    word = word.lower()
    lower_candidates = [word.lower() for word in candidates]

    anagrams = []

    for index, candidate_word in enumerate(lower_candidates):
        if check_samechar_count(word, candidate_word) and word != candidate_word:
            anagrams.append(candidates[index])
    return anagrams
