def roman_to_integer(roman):
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

    i = 0
    j = 1
    result = 0

    if len(roman) == 1:
        result = conversion_map[roman]
    else:
        while i <= len(roman) - 1:
            if roman[i:j + 1] in conversion_map:
                result += conversion_map[roman[i:j + 1]]
                i += 2
                j += 2
            else:
                result += conversion_map[roman[i]]
                i += 1
                j += 1

    return result


def roman_to_integer_leetcode_solution(roman):
    conversion_map = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    result = 0
    for i in range(len(roman)):
        if i + 1 <= len(roman) - 1 and conversion_map[roman[i]] < conversion_map[roman[i + 1]]:
            result -= conversion_map[roman[i]]
        else:
            result += conversion_map[roman[i]]

    return result
