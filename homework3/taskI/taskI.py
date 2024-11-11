class Rover:

    def __init__(self, ind, arrival_time: int, direction: int):
        self.arrival_time = arrival_time
        self.direction = direction
        self.crossing = None
        self.ind = ind

    def set_crossing(self, minute: int) -> None:
        # print("rover:", self.ind, "crossing on minute:", minute)
        self.crossing = minute

    def __repr__(self):
        return str((self.ind, self.arrival_time, self.direction, self.crossing))


def determine_priority_of_road_parts(a, b) -> tuple[int, int, int, int]:
    if abs(a - b) == 2:
        lst = [2, 2, 2, 2]
        lst[a - 1] = 1
        lst[b - 1] = 1
        return tuple(lst)

    elif a in {1, 2} and b in {1, 2}:
        return (1, 2, 3, 4)
    elif a in {1, 4} and b in {1, 4}:
        return (2, 3, 4, 1)
    elif a in {3, 4} and b in {3, 4}:
        return (3, 4, 1, 2)
    elif a in {3, 2} and b in {3, 2}:
        return (4, 1, 2, 3)
    else:
        raise ArithmeticError(f"unpredictable a and b: {a, b}")


def find_time_of_rovers_crossing_the_intersection(
        n: int,
        a: int,
        b: int,
        rovers_data: list[list[int]],
) -> list[int]:

    priorities = determine_priority_of_road_parts(a, b)

    rovers = [Rover(ind, minute, direction) for ind, (direction, minute) in enumerate(rovers_data, start=1)]
    rovers.sort(key=lambda x: x.arrival_time)

    ready_to_go_1 = list()
    ready_to_go_2 = list()
    ready_to_go_3 = list()
    ready_to_go_4 = list()

    queues = (ready_to_go_1, ready_to_go_2, ready_to_go_3, ready_to_go_4)

    ind = 0

    for minute in range(1, 1000):

        while ind < len(rovers) and rovers[ind].arrival_time <= minute:
            rover = rovers[ind]
            ind += 1

            if rover.direction == 1:
                ready_to_go_1.append(rover)
            elif rover.direction == 2:
                ready_to_go_2.append(rover)
            elif rover.direction == 3:
                ready_to_go_3.append(rover)
            elif rover.direction == 4:
                ready_to_go_4.append(rover)
            else:
                raise ValueError(f"Invalid value for direction: {rover.direction}")

        for priority in range(1, 5):
            goes = False
            for i, queue in enumerate(queues):
                if queue:
                    if priorities[i] == priority:
                        rover_to_go = queue.pop(0)
                        rover_to_go.set_crossing(minute)
                        goes = True
            if goes:
                break

    rovers.sort(key=lambda x: x.ind)
    return [rover.crossing for rover in rovers]


if __name__ == "__main__":
    n = int(input())
    a, b = map(int, input().split())
    rovers_data = []
    for _ in range(n):
        rovers_data.append(list(map(int, input().split())))
    res = find_time_of_rovers_crossing_the_intersection(n, a, b, rovers_data)
    print(*res, sep="\n")
