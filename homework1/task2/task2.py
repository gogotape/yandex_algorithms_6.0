def find_min_numbers_of_socks_and_t_shorts(blue_t, red_t, blue_s, red_s) -> tuple[int, int]:
    """
    :return: M (T shorts) and N (socks)
    """

    if blue_t == 0:
        return 1, blue_s + 1

    if red_t == 0:
        return 1, red_s + 1

    if blue_s == 0:
        return blue_t + 1, 1

    if red_s == 0:
        return red_t + 1, 1

    var1 = max(blue_t, red_t) + 1, 1
    var2 = 1, max(blue_s, red_s) + 1
    var3 = (min(blue_t, red_t) + 1, min(blue_s, red_s) + 1) if (blue_t > red_t and blue_s > red_s) or (blue_t < red_t and blue_s < red_s) else (float("inf"), float("inf"))
    var4 = blue_t + red_t, 1
    var5 = 1, blue_s + red_s

    variants = [var1, var2, var3, var4, var5]
    return min(variants, key=lambda x: x[0] + x[1])


if __name__ == "__main__":
    a, b, c, d = map(int, (input() for _ in range(4)))
    res = find_min_numbers_of_socks_and_t_shorts(a, b, c, d)
    print(res[0], res[1])
