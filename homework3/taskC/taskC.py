def find_min_values_on_segments(nums: list[int], k: int) -> list[int]:

    result = []

    stack = []
    for i in range(k):
        while stack and nums[i] < stack[-1][-1]:
            stack.pop()
        stack.append((i, nums[i]))
    if stack:
        result.append(stack[0][-1])

    for j, num in enumerate(nums[k:], start=k):
        if stack[0][0] + k <= j:
            stack.pop(0)
        while stack and num < stack[-1][-1]:
            stack.pop()
        stack.append((j, num))
        result.append(stack[0][-1])

    return result


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    res = find_min_values_on_segments(nums, k)
    for num in res:
        print(num)
