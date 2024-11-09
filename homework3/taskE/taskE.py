def calc_postfix_statement(lst: list[str]) -> int:
    stack = []
    for char in lst:
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


def group_digits_in_nums(s: str) -> list[str]:
    i = 0
    items = []
    while i < len(s):
        char = s[i]
        if char.isdigit():
            num = char
            while i + 1 < len(s) and s[i + 1].isdigit():
                num += s[i + 1]
                i += 1
            items.append(num)
        else:
            items.append(char)
        i += 1
    return items


def find_nums_indices(items: list[str]) -> list[int]:
    indices = []
    for index, item in enumerate(items):
        if item.isdigit():
            indices.append(index)
    return indices


def check_string(s: str) -> None:
    grouped = group_digits_in_nums(s)
    indices = find_nums_indices(grouped)

    if len(indices) < 2:
        return

    l, r = 0, 1

    while r < len(indices):
        left, right = indices[l], indices[r]
        if "".join(grouped[left+1:right]) == " " * (right - left - 1) and (right - left) != 1:
            raise ValueError("spaces between digits!")
        else:
            l += 1
            r += 1


def infix_to_postfix(s: str) -> list[str]:

    check_string(s)
    s = s.replace(" ", "")

    res = []
    stack = []

    i = 0
    while i < len(s):

        char = s[i]

        if char == "(":
            stack.append(char)
        elif char.isdigit():
            num = char
            while i + 1 < len(s) and s[i + 1].isdigit():
                num += s[i + 1]
                i += 1
            res.append(num)

        elif char in ["+", "-"]:
            while stack and (stack[-1] in ("+", "-", "*")):
                res.append(stack.pop())
            stack.append(char)
        elif char == "*":
            while stack and stack[-1] == "*":
                res.append(stack.pop())
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(" and (stack[-1] in ("+", "-", "*")):
                res.append(stack.pop())
            stack.pop()
        else:
            raise ValueError(f"invalid char: {char}")

        i += 1

    while stack:
        res.append(stack.pop())

    return res


def calc_arithmetic_statement(infix: str) -> str:
    try:
        postfix = infix_to_postfix(infix)
        res = calc_postfix_statement(postfix)
    except Exception:
        return "WRONG"
    return str(res)


if __name__ == "__main__":
    s = input()
    res = calc_arithmetic_statement(s)
    print(res)
