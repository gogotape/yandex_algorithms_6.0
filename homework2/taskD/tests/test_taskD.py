from homework2.taskD.taskD import calc_min_days_for_vacation


def test_taskD():
    k = 2
    directions = [4, 2, 1]
    assert calc_min_days_for_vacation(k, directions) == 2

    k = 2
    directions = [3, 8, 5, 7, 1, 2, 4, 9, 6]
    assert calc_min_days_for_vacation(k, directions) == 3

    k = 0
    directions = [1, 3, 1]
    assert calc_min_days_for_vacation(k, directions) == 2

    k = 4
    directions = [32, 77, 1, 100]
    assert calc_min_days_for_vacation(k, directions) == 1
