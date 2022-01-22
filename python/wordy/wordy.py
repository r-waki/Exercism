import re

def answer(question):
    question = question.replace('?', '')
    question = question.replace(' by', '')
    question_sentence = [word for word in question.split()]
    question_sentence = question_sentence[2:]

    for calclate()



    if len(question_sentence) == 1:
        return int(question_sentence[0])
    elif len(question_sentence) == 3 and question_sentence[1] == "plus":
        return int(question_sentence[0]) + int(question_sentence[2])
    elif len(question_sentence) == 3 and question_sentence[1] == "minus":
        return int(question_sentence[0]) - int(question_sentence[2])
    elif len(question_sentence) == 4 and question_sentence[1:3] == ["multiplied", "by"]:
        return int(question_sentence[0]) * int(question_sentence[3])
    elif len(question_sentence) == 4 and question_sentence[1:3] == ["divided", "by"]:
        return int(question_sentence[0]) / int(question_sentence[3])

def is_number(n):
    re.compile(r"\d")
    if type(n) != int:
        raise ValueError("not the number!!")
    return True

def is_arithmetic_operations(n):
    arithmetic_operations = set("plus", "minus", "multiplied", "divided")

    if arithmetic_operations.disjoined(n):
        raise ValueError("not the arithmetic operations")
    return True

def calclate(question):

    if len(question) == 1:
        return int(question[0])

    is_number(question[0])
    is_number(question[2])
    is_arithmetic_operations(question[1])

    if operation == "plus":
        return int(x) + int(y)
    elif operation == "minus":
        return int(x) - int(y)
    elif operation == "multiplied":
        return int(x) * int(y)
    else:
        return int(x) / int(y)
