def find_cities_to_move(cities: list[int]) -> list[int]:
    cities_to_move = [-1] * len(cities)
    stack = []

    for i, city in enumerate(cities):
        while stack and city < stack[-1][-1]:
            ind, popped_city = stack.pop()
            cities_to_move[ind] = i
        stack.append((i, city))

    return cities_to_move


if __name__ == "__main__":
    n = int(input())
    cities = list(map(int, input().split()))
    res = find_cities_to_move(cities)
    print(*res)
