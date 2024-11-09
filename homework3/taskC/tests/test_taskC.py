from homework3.taskC.taskC import find_min_values_on_segments


def test_taskC():
    nums = [1, 3, 2, 4, 5, 3, 1]
    k = 3
    assert find_min_values_on_segments(nums, k) == [1, 2, 2, 3, 1]

    nums = []
    k = 0
    assert find_min_values_on_segments(nums, k) == []

    nums = [1]
    k = 1
    assert find_min_values_on_segments(nums, k) == [1]

    nums = [3, 1, 2]
    k = 1
    assert find_min_values_on_segments(nums, k) == [3, 1, 2]

    nums = [3, 1, 2]
    k = 2
    assert find_min_values_on_segments(nums, k) == [1, 1]

    nums = [3, 1, 2]
    k = 3
    assert find_min_values_on_segments(nums, k) == [1]

    nums = [3, 5, 100, 20, 10, 20, 10, 10, 10, 10, 10, 12, -1]
    k = 3
    assert find_min_values_on_segments(nums, k) == [3, 5, 10, 10, 10, 10, 10, 10, 10, 10, -1]

    nums = [1, 1, 1, 1, 1]
    k = 4
    assert find_min_values_on_segments(nums, k) == [1, 1]

    nums = [1, 1, 1, 1, 1]
    k = 2
    assert find_min_values_on_segments(nums, k) == [1, 1, 1, 1]

    nums = [1, 1, 1, 1, 1]
    k = 5
    assert find_min_values_on_segments(nums, k) == [1]
