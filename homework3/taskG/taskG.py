def calc_total_minutes_for_clients(
        clients_comes_on_minute: list[int],
        b: int,
) -> int:

    total_waiting = 0
    clients = 0
    for clients_on_minutes in clients_comes_on_minute:
        clients += clients_on_minutes
        total_waiting += clients
        clients -= min(clients, b)

    return total_waiting + clients


if __name__ == "__main__":
    n, b = map(int, input().split())
    clients_comes_on_minute = list(map(int, input().split()))
    res = calc_total_minutes_for_clients(clients_comes_on_minute, b)
    print(res)
