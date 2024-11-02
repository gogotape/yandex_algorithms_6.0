def calc_numbers_of_possible_ways_to_organize_dates(
        monuments: list[int],
        fog_distance: int,
) -> int:

    l, r = 0, 1
    counter = 0

    while r < len(monuments):
        distance = monuments[r] - monuments[l]
        if distance > fog_distance:
            counter += len(monuments) - r
            l += 1
        else:
            r += 1

    return counter


if __name__ == "__main__":
    n, fog_distance = map(int, (input().split()))
    monuments = list(map(int, input().split()))
    res = calc_numbers_of_possible_ways_to_organize_dates(
        monuments,
        fog_distance,
    )
    print(res)
