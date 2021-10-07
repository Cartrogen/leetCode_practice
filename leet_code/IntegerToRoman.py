def integer_to_roman(number):
    conversion_map = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    result = ""

    for roman, value in conversion_map.items():
        if number / value >= 1:
            count = number // value
            result += count * roman
            number = number % value

    return result

