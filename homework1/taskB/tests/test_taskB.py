from homework1.taskB.taskB import find_min_numbers_of_socks_and_t_shorts


def test_taskB():
    a, b, c, d = 6, 2, 7, 3
    assert find_min_numbers_of_socks_and_t_shorts(a, b, c, d) == (3, 4)

    a = b = c = d = 1
    assert find_min_numbers_of_socks_and_t_shorts(a, b, c, d) == (2, 1)

    a, b, c, d = 9, 0, 5, 2
    assert find_min_numbers_of_socks_and_t_shorts(a, b, c, d) == (1, 3)

    a, b, c, d = 0, 2, 5, 1
    assert find_min_numbers_of_socks_and_t_shorts(a, b, c, d) == (1, 6)

    a, b, c, d = 10, 7, 0, 4
    assert find_min_numbers_of_socks_and_t_shorts(a, b, c, d) == (11, 1)

    a, b, c, d = 5, 6, 7, 0
    assert find_min_numbers_of_socks_and_t_shorts(a, b, c, d) == (7, 1)

    a, b, c, d = 114, 299, 921, 166
    assert find_min_numbers_of_socks_and_t_shorts(a, b, c, d) == (300, 1)
