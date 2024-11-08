from homework3.taskB.taskB import find_cities_to_move


def test_taskB():
    cities = [1, 2, 3, 2, 1, 4, 2, 5, 3, 1]
    assert find_cities_to_move(cities) == [-1, 4, 3, 4, -1, 6, 9, 8, 9, -1]

    cities = [5, 3, 1]
    assert find_cities_to_move(cities) == [1, 2, -1]

    cities = [10, 1]
    assert find_cities_to_move(cities) == [1, -1]

    cities = [1, 10]
    assert find_cities_to_move(cities) == [-1, -1]

    cities = [1, 2, 3, 4, 5, 6]
    assert find_cities_to_move(cities) == [-1] * 6

    cities = [6, 5, 4, 3, 2, 1]
    assert find_cities_to_move(cities) == [1, 2, 3, 4, 5, -1]
