def calc_number_sets_of_cars(cars: list[int], k: int) -> int:

    prefix_sum_arr = calc_prefix_sum(cars)
    l, r = 0, 1
    counter = 0

    while r <= len(cars):
        summ = prefix_sum_arr[r] - prefix_sum_arr[l]
        if summ == k:
            counter += 1
            l += 1
        elif summ < k:
            r += 1
        else:
            l += 1

    return counter


def calc_prefix_sum(arr: list[int]) -> list[int]:
    prefix_sum_arr = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_sum_arr[i] = prefix_sum_arr[i - 1] + arr[i - 1]
    return prefix_sum_arr


if __name__ == "__main__":
    n, k = map(int, (input().split()))
    cars = list(map(int, input().split()))
    res = calc_number_sets_of_cars(cars, k)
    print(res)
