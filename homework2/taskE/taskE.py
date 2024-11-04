def find_order_of_deleting_medians(arr: list[int]) -> list[int]:

    arr.sort()

    order_of_deleting = []

    while arr:
        if len(arr) % 2 == 0:
            ind = len(arr) // 2 - 1
        else:
            ind = len(arr) // 2
        order_of_deleting.append(arr.pop(ind))

    return order_of_deleting


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    res = find_order_of_deleting_medians(nums)
    print(*res)
