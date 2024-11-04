def calc_min_days_for_vacation(
        k: int,
        directions: list[int],
) -> int:

    directions.sort()

    l, r = 0, 1
    max_days = 1

    while r < len(directions):
        diff = abs(directions[r] - directions[l])
        if diff <= k:
            max_days = max(max_days, r - l + 1)
        else:
            l += 1
        r += 1

    return max_days


if __name__ == "__main__":
    n, k = map(int, (input().split()))
    directions = list(map(int, input().split()))
    res = calc_min_days_for_vacation(k=k, directions=directions)
    print(res)
