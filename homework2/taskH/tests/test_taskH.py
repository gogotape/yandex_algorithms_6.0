from homework2.taskH.taskH import calc_min_numbers_of_transitions, dummy


def test_taskH():
    cabinets = [5, 2, 3, 1]
    assert dummy(cabinets) == 10
    assert calc_min_numbers_of_transitions(cabinets) == 10

    cabinets = [5, 4, 3, 2, 1]
    assert dummy(cabinets) == 15
    assert calc_min_numbers_of_transitions(cabinets) == 15

    cabinets = [1, 2, 3, 4, 5]
    assert dummy(cabinets) == 15
    assert calc_min_numbers_of_transitions(cabinets) == 15

    cabinets = [100]
    assert dummy(cabinets) == 0
    assert calc_min_numbers_of_transitions(cabinets) == 0
