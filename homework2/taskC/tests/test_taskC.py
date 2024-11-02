from homework2.taskC.taskC import calc_numbers_of_possible_ways_to_organize_dates


def test_taskC():
    monuments = [1, 3, 5, 8]
    k = 4
    assert calc_numbers_of_possible_ways_to_organize_dates(monuments, k) == 2

    monuments = [1, 3, 5, 8]
    k = 7
    assert calc_numbers_of_possible_ways_to_organize_dates(monuments, k) == 0

    monuments = [1, 10]
    k = 5
    assert calc_numbers_of_possible_ways_to_organize_dates(monuments, k) == 1

    monuments = [1, 10]
    k = 9
    assert calc_numbers_of_possible_ways_to_organize_dates(monuments, k) == 0

    monuments = [1, 2, 5, 7, 13]
    k = 2
    assert calc_numbers_of_possible_ways_to_organize_dates(monuments, k) == 8
