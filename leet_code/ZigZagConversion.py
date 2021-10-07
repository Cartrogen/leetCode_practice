def zigzag_conversion(s, num_rows):
    generic_increment = (num_rows - 1) * 2
    final_string = ""

    for r in range(num_rows):
        for i in range(r, len(s), generic_increment):
            final_string = final_string + s[i]

            if 0 < r < num_rows - 1 and i + generic_increment - (2 * r) < len(s):
                final_string = final_string + s[i + generic_increment - 2 * r]

    return final_string
