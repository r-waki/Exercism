import queue


def is_paired(input_string):

    open_brackets = ["[", "{", "("]
    close_brackets = ["]", "}", ")"]
    brackets_pair = {"]": "[", "}": "{", ")": "("}
    open_queue = queue.LifoQueue(maxsize=0)

    for word in input_string:
        if word in open_brackets:
            open_queue.put(word)
        elif word in close_brackets:
            try:
                open_bracket = open_queue.get(timeout=1)
            except queue.Empty:
                return False

            if (brackets_pair[word] != open_bracket):
                return False
        else:
            continue

    if open_queue.empty():
        return True
    else:
        return False
