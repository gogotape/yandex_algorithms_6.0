def calc_prefix_sum(array: list[int]) -> list[int]:
    prefix_sum_arr = [0] * (len(array) + 1)
    for i in range(1, len(array) + 1):
        prefix_sum_arr[i] = array[i - 1] + prefix_sum_arr[i - 1]
    return prefix_sum_arr[1:]


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    res = calc_prefix_sum(arr)
    print(*res)
