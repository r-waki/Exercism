def prime(number):
    prime_numbers = prime_range(number)
    return prime_numbers[number - 1]


def prime_range(number):
    if number <= 0:
        raise ValueError("number is not essential number")
    checked_number = 3
    prime_numbers = [2]

    while len(prime_numbers) != number:
        for n in prime_numbers:
            if checked_number % n == 0:
                break
            if n == prime_numbers[-1]:
                prime_numbers.append(checked_number)

        checked_number += 1

    return prime_numbers
