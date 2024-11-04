from homework2.taskE.taskE import find_order_of_deleting_medians


def test_taskE():
    nums = [19, 3, 8]
    assert find_order_of_deleting_medians(nums) == [8, 3, 19]

    nums = [1, 2, 4, 2]
    assert find_order_of_deleting_medians(nums) == [2, 2, 1, 4]
