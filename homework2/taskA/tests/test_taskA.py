from homework2.taskA.taskA import calc_prefix_sum


def test_calc_prefix_sum():
    arr1 = [10, -4, 5, 0, 2]
    assert calc_prefix_sum(arr1) == [10, 6, 11, 11, 13]

    arr2 = []
    assert calc_prefix_sum(arr2) == []

    arr3 = [2, 3]
    assert calc_prefix_sum(arr3) == [2, 5]

    arr4 = [7]
    assert calc_prefix_sum(arr4) == [7]
