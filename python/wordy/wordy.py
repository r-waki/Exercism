def answer(question):
    question = question.replace('?', '')
    question = question.replace(' by', '')
    question = [word for word in question.split()]
    question = question[2:]

    if not question:
        raise ValueError("no questions")

    if len(question) == 2:
        raise ValueError("invalid statement")

    arithmetic_operations = ["plus", "minus", "multiplied", "divided"]

    for i, q in enumerate(question):
        if i == 0:
            ans = int(q)

        elif i % 2 == 1 and q not in arithmetic_operations:
            raise ValueError("not arithmetic operations")

        elif i % 2 == 1 and q in arithmetic_operations:
            operation = q

        elif i % 2 == 0:

            if operation == "plus":
                ans = ans + int(q)
            elif operation == "minus":
                ans = ans - int(q)
            elif operation == "multiplied":
                ans = ans * int(q)
            elif operation == "divided":
                ans = ans / int(q)

    return ans
