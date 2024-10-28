from homework1.taskA.taskA import determine_closest_raft_side_or_edge


def test_taskA():
    x1, y1 = -1, -2
    x2, y2 = 5, 3
    x, y = -4, 6

    assert determine_closest_raft_side_or_edge(x1, y1, x2, y2, x, y) == "NW"
