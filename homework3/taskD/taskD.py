def calc_postfix_statement(s: str) -> int:
    s.rstrip()
    s = s.replace(" ", "")
    stack = []
    for char in s:
        if char.isdigit():
            stack.append(char)
        else:
            second = int(stack.pop())
            first = int(stack.pop())
            if char == "+":
                res = first + second
            elif char == "*":
                res = first * second
            elif char == "-":
                res = first - second
            else:
                raise ValueError(f"incorrect operator: {char}")
            stack.append(int(res))

    return int(stack[0])


if __name__ == "__main__":
    s = input()
    res = calc_postfix_statement(s)
    print(res)
