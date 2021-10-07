def fizz_buzz(n):
    result = ""
    result_array = []

    for number in range(1, n + 1):
        if number % 3 == 0:
            result += "Fizz"
        if number % 5 == 0:
            result += "Buzz"
        if number % 3 != 0 and number % 5 != 0:
            result = str(number)

        result_array.append(result)
        result = ""

    return result_array
