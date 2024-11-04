def calc_sum_of_triple_multiplications(arr: list[int]) -> int:
    prefix_sum_arr = calc_prefix_sum(arr)
    prefix_prod_sum = calc_prefix_prod_sum(arr, prefix_sum_arr)
    prefix_sum_prod_arr = calc_prefix_sum(prefix_prod_sum)

    res = 0
    for i in range(len(arr) - 1):
        res += arr[i] * (prefix_sum_prod_arr[-1] - prefix_sum_prod_arr[i])
    return res % 1000000007


def calc_prefix_sum(arr: list[int]) -> list[int]:
    prefix_sum_arr = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_sum_arr[i] = prefix_sum_arr[i - 1] + arr[i - 1]
    return prefix_sum_arr[1:]


def calc_prefix_prod_sum(arr: list[int], prefix_sum_arr: list[int]) -> list[int]:
    prefix_prod_sum = [0] * len(prefix_sum_arr)
    for i in range(len(prefix_sum_arr)):
        coeff = arr[i]
        diff = prefix_sum_arr[-1] - prefix_sum_arr[i]
        prefix_prod_sum[i] = coeff * diff
    return prefix_prod_sum


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    res = calc_sum_of_triple_multiplications(nums)
    print(res)
