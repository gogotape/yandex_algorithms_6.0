from homework3.taskI.taskI import find_time_of_rovers_crossing_the_intersection, determine_priority_of_road_parts


def test_determine_priority_of_road_parts():
    a, b = 1, 3
    assert determine_priority_of_road_parts(a, b) == (1, 2, 1, 2)

    a, b = 3, 1
    assert determine_priority_of_road_parts(a, b) == (1, 2, 1, 2)

    a, b = 2, 4
    assert determine_priority_of_road_parts(a, b) == (2, 1, 2, 1)

    a, b = 4, 2
    assert determine_priority_of_road_parts(a, b) == (2, 1, 2, 1)

    a, b = 1, 2
    assert determine_priority_of_road_parts(a, b) == (1, 2, 3, 4)

    a, b = 2, 3
    assert determine_priority_of_road_parts(a, b) == (4, 1, 2, 3)

    a, b = 3, 2
    assert determine_priority_of_road_parts(a, b) == (4, 1, 2, 3)

    a, b = 3, 4
    assert determine_priority_of_road_parts(a, b) == (3, 4, 1, 2)

    a, b = 4, 3
    assert determine_priority_of_road_parts(a, b) == (3, 4, 1, 2)

    a, b = 1, 4
    assert determine_priority_of_road_parts(a, b) == (2, 3, 4, 1)

    a, b = 4, 1
    assert determine_priority_of_road_parts(a, b) == (2, 3, 4, 1)


def test_find_time_of_rovers_crossing_the_intersection():
    n = 4
    a, b = 1, 3
    rovers = [
        [1, 1],
        [3, 1],
        [2, 1],
        [2, 2],
    ]
    assert find_time_of_rovers_crossing_the_intersection(n, a, b, rovers) == [1, 1, 2, 3]


def test_find_time_of_rovers_crossing_the_intersection_2():
    n = 4
    a, b = 1, 2
    rovers = [
        [1, 1],
        [2, 1],
        [3, 1],
        [4, 1],
    ]
    assert find_time_of_rovers_crossing_the_intersection(n, a, b, rovers) == [1, 2, 3, 4]


def test_find_time_of_rovers_crossing_the_intersection_3():
    n = 1
    a, b = 1, 4
    rovers = [
        [1, 1],
    ]
    assert find_time_of_rovers_crossing_the_intersection(n, a, b, rovers) == [1]


def test_find_time_of_rovers_crossing_the_intersection_4():
    n = 1
    a, b = 1, 4
    rovers = [
        [3, 100],
    ]
    assert find_time_of_rovers_crossing_the_intersection(n, a, b, rovers) == [100]


def test_find_time_of_rovers_crossing_the_intersection_5():
    n = 1
    a, b = 1, 4
    rovers = [
        [3, 100],
    ]
    assert find_time_of_rovers_crossing_the_intersection(n, a, b, rovers) == [100]


def test_find_time_of_rovers_crossing_the_intersection_6():
    n = 1
    a, b = 1, 4
    rovers = [
        [3, 1],
    ]
    assert find_time_of_rovers_crossing_the_intersection(n, a, b, rovers) == [1]
