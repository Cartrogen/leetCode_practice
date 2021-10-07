def valid_parenthesis(str):
    bracket_map = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    bracket_stack = []

    for bracket in str:
        if bracket in bracket_map:
            if bracket_stack and [bracket] == bracket_stack[-1]:
                bracket_stack.pop()
            else:
                return False
        else:
            bracket_stack.append(bracket)

    return True if len(bracket_stack) == 0 else False
