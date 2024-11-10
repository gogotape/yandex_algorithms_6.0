from homework3.taskG.taskG import calc_total_minutes_for_clients


def test_calc_total_minutes_for_clients():
    b = 4
    clients_per_minutes = [1, 5, 9]
    assert calc_total_minutes_for_clients(clients_per_minutes, b) == 22

    b = 1000
    clients_per_minutes = [5, 100, 500, 200, 14]
    assert calc_total_minutes_for_clients(clients_per_minutes, b) == sum(clients_per_minutes)

    b = 2
    clients_per_minutes = [2, 3]
    assert calc_total_minutes_for_clients(clients_per_minutes, b) == (2 + 2 + 2)

    b = 5
    clients_per_minutes = [10]
    assert calc_total_minutes_for_clients(clients_per_minutes, b) == (5 + 5 * 2)

    b = 2
    clients_per_minutes = [2]
    assert calc_total_minutes_for_clients(clients_per_minutes, b) == 2

    b = 2
    clients_per_minutes = [1]
    assert calc_total_minutes_for_clients(clients_per_minutes, b) == 1

    b = 2
    clients_per_minutes = [1, 0, 0, 0]
    assert calc_total_minutes_for_clients(clients_per_minutes, b) == 1

    b = 2
    clients_per_minutes = [0, 0, 0, 0]
    assert calc_total_minutes_for_clients(clients_per_minutes, b) == 0

    b = 3
    clients_per_minutes = [2, 5, 7, 9, 11]
    assert calc_total_minutes_for_clients(clients_per_minutes, b) == 74

