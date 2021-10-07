def longest_palindromic_string(s):
    longest_string = ""
    longest_string_length = 0
    # odd
    for n in range(len(s)):
        r = n
        l = n
        while r < len(s) and l >= 0 and s[l] == s[r]:
            temp_longest_string = s[l:r + 1]
            if len(temp_longest_string) > longest_string_length:
                longest_string = s[l:r + 1]
                longest_string_length = len(temp_longest_string)
            r += 1
            l -= 1

        # r = n + 1
        # l = n
        # while r < len(s) and l >= 0 and s[l] == s[r]:
        #     temp_longest_string = s[l:r + 1]
        #     if len(temp_longest_string) > longest_string_length:
        #         longest_string = s[l:r + 1]
        #         longest_string_length = len(temp_longest_string)
        #     r += 1
        #     l -= 1

    return "Longest string is - ", longest_string, "longest string length is - ", longest_string_length
