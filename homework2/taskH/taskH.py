def calc_prefix_sum(arr: list[int]) -> list[int]:
    prefix_sum = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    return prefix_sum


def calc_suffix_sum(arr: list[int]) -> list[int]:
    suffix_sum = [0] * (len(arr) + 1)
    for i in range(len(arr) - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + arr[i]
    return suffix_sum


def calc_min_numbers_of_transitions(cabinets: list[int]) -> int:
    left_to_right = calc_prefix_sum(cabinets)[1:]
    right_to_left = calc_suffix_sum(cabinets)[:-1]
    prefix_sum = calc_prefix_sum(left_to_right)
    suffix_sum = calc_suffix_sum(right_to_left)

    res = float("inf")
    for i in range(len(cabinets)):
        cur_res = prefix_sum[i] + suffix_sum[i + 1]
        res = min(res, cur_res)
    return res


def dummy(cabinets: list[int]) -> int:
    res = float("inf")
    for i in range(len(cabinets)):
        cur_res = 0
        for j in range(len(cabinets)):
            cur_res += cabinets[j] * abs(j - i)
        res = min(res, cur_res)
    return res


if __name__ == "__main__":
    n = int(input())
    cabinets = list(map(int, input().split()))
    res = calc_min_numbers_of_transitions(cabinets)
    print(res)
