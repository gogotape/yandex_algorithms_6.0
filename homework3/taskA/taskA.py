from typing import Literal


def is_correct_bracket_sequence(s: str) -> Literal["yes", "no"]:

    brackets = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    stack = []

    for char in s:
        if char not in brackets:
            stack.append(char)
        else:
            if not stack:
                return "no"
            if stack[-1] != brackets[char]:
                return "no"
            else:
                stack.pop()
    return "no" if stack else "yes"


if __name__ == "__main__":
    s = input()
    res = is_correct_bracket_sequence(s)
    print(res)
