def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    scores = [round(score) for score in student_scores]
    scores.reverse()
    return scores


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    return sum([score <= 40 for score in student_scores])


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """
    difference = (highest - 40) / 4
    difference = round(difference)
    score_thresholds = [41]
    for i in range(0, 3):
        score_thresholds.append(score_thresholds[i] + difference)

    return score_thresholds


def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    student_ranking = []
    for index, scores in enumerate(student_scores):
        student_ranking.append(f"{index + 1}. {student_names[index]}: {scores}")
    return student_ranking


def perfect_score(students_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """
    for student_info in students_info:
        score = student_info[1]
        if score == 100:
            return student_info

    return "No perfect score."
