from homework2.taskF.taskF import calc_sum_of_triple_multiplications


def test_taskF():
    nums = [1, 2, 3]
    assert calc_sum_of_triple_multiplications(nums) == 6

    nums = [0, 5, 6, 7]
    assert calc_sum_of_triple_multiplications(nums) == 210

    nums = [1, 2, 3, 4]
    assert calc_sum_of_triple_multiplications(nums) == 50

    nums = [10, 6, 10, 3, 7]
    assert calc_sum_of_triple_multiplications(nums) == 3346

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert calc_sum_of_triple_multiplications(nums) == 18150
