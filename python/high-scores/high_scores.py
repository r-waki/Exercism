def latest(scores):
    return scores[len(scores)-1]


def personal_best(scores):
    scores.sort()
    best_score =  scores.pop()
    return best_score


def personal_top_three(scores):
    scores.sort()
    
    num = 1
    top_three_score = list()

    while (num < 4):
        top_three_score.append(scores.pop()) 

        num += 1

        if len(scores) == 0 :
            break

    return top_three_score