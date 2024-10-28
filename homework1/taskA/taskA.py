def calculate_distance_between_two_points(x1, y1, x2, y2) -> float:
    return ( (x1 - x2) ** 2 + (y2 - y1) ** 2) ** 0.5


class Point:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.distance_to_swimmer = None


def determine_closest_raft_side_or_edge(x1, y1, x2, y2, x, y) -> str:

    NW = x1, y2
    NE = x2, y2
    SW = x1, y1
    SE = x2, y1

    points = [Point(*points, name) for points, name in zip((NW, NE, SW, SE), ("NW", "NE", "SW", "SE"))]

    for point in points:
        edge_x, edge_y = point.x, point.y
        distance = calculate_distance_between_two_points(edge_x, edge_y, x, y)
        point.distance_to_swimmer = distance

    if y1 < y < y2:
        point = Point(None, None, "W")
        distance = calculate_distance_between_two_points(x, y, x1, y)
        point.distance_to_swimmer = distance
        points.append(point)

        point = Point(None, None, "E")
        distance = calculate_distance_between_two_points(x, y, x2, y)
        point.distance_to_swimmer = distance
        points.append(point)

    if x1 < x < x2:
        point = Point(None, None, "N")
        distance = calculate_distance_between_two_points(x, y, x, y2)
        point.distance_to_swimmer = distance
        points.append(point)

        point = Point(None, None, "S")
        distance = calculate_distance_between_two_points(x, y, x, y1)
        point.distance_to_swimmer = distance
        points.append(point)

    p = min(points, key=lambda x: x.distance_to_swimmer)
    return p.name


if __name__ == "__main__":
    x1, y1, x2, y2, x, y = map(int, [input() for _ in range(6)])
    print(determine_closest_raft_side_or_edge(x1, y1, x2, y2, x, y))






