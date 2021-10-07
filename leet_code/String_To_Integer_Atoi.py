def string_to_integer_atoi(str):
    result = 0
    is_negative = False
    is_recording = False

    for i in range(len(str)):
        if str[i] == " " and is_recording is False:
            continue
        if str[i] == " " and str[i - 1] != " ":
            break
        if str[i] == "-":
            if is_recording is False:
                is_negative = True
                is_recording = True
                continue
            else:
                break
        if str[i] == "+":
            if is_recording is False:
                is_recording = True
                continue

            else:
                break
        ascii_val = ord(str[i]) - ord("0")
        if 0 <= ascii_val <= 9:
            result = (result * 10) + ascii_val
            is_recording = True
        else:
            break

    if is_negative:
        result = 0 - result

    if result < -2 ** 31:
        return -2 ** 31
    elif result > (2 ** 31) - 1:
        return (2 ** 31) - 1
    else:
        return result
