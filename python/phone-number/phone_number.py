import re


class PhoneNumber:
    def __init__(self, number):
        table = str.maketrans({
            '(': '',
            ')': '',
            ' ': '',
            '.': '',
            '-': ''
        })
        number = number.translate(table)

        if number[0:2] == "+1":
            number = number[2::]
        elif number[0] == "1":
            number = number[1::]

        if re.match(r"(?![0-9]+)", number):
            raise ValueError("Please input the number")
        elif re.match(r"(?!^[2-9])", number):
            raise ValueError("First digit is not [2-9]")
        elif re.match(r"(?!^.{3}[2-9])", number):
            raise ValueError("Four digit is not [2-9]")
        elif len(number) != 10:
            raise ValueError("number is not 10 digit")

        self.number = number
        self.area_code = number[0:3]

    def pretty(self):
        full_number = list(self.number)
        full_number.insert(0, "(")
        full_number.insert(4, ")-")
        full_number.insert(8, "-")
        return "".join(full_number)
