import math


def reverse_integer(number):
    reverse = 0
    while number:
        remainder = int(math.fmod(number, 10))
        reverse = (reverse * 10) + remainder

        if number < 0:
            number = math.ceil(number / 10)
        else:
            number = math.floor(number / 10)

        if reverse > (2 ** 31) - 1:
            return 0
        if reverse < (-2 ** 31):
            return 0

    return reverse
