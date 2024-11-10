def find_lexical_min_correct_bracket_sequence(n: int, w: str, s: str) -> str:

    priorities = {}
    for i, bracket in enumerate(w):
        priorities[bracket] = i

    to_open = "(" if priorities["("] < priorities["["] else "["
    stack = []
    for bracket in s:
        if bracket in ("(", "["):
            stack.append(bracket)
        else:
            if stack:
                top = stack[-1]
                if top == "[" and bracket == "]":
                    stack.pop()
                elif top == "(" and bracket == ")":
                    stack.pop()

    result = s[:]

    opens = 0
    for bracket in stack:
        if bracket in ("(", "["):
            opens += 1

    steps = n - len(s)

    for step in range(steps):
        if n - len(s) - step == opens:
            while stack:
                top = stack[-1]
                if top == "(":
                    result += ")"
                elif top == "[":
                    result += "]"
                else:
                    pass
                stack.pop()
            break

        if not stack:
            stack.append(to_open)
            result += to_open
            opens += 1
            continue

        if stack[-1] in ("[", "("):
            open_bracket = stack[-1]
            to_close = ")" if open_bracket == "(" else "]"
            if priorities[to_close] < priorities[to_open]:
                stack.pop()
                result += to_close
                opens -= 1
            else:
                stack.append(to_open)
                result += to_open
                opens += 1
    return result


if __name__ == "__main__":
    n = int(input())
    w = input()
    s = input()
    res = find_lexical_min_correct_bracket_sequence(n, w, s)
    print(res)
