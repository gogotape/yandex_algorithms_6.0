from homework2.taskB.taskB import calc_number_sets_of_cars


def test_taskB():
    cars = [17, 7, 10, 7, 10]
    k = 17
    assert calc_number_sets_of_cars(cars, k) == 4

    cars = [1, 2, 3, 4, 1]
    k = 10
    assert calc_number_sets_of_cars(cars, k) == 2

    cars = [5]
    k = 5
    assert calc_number_sets_of_cars(cars, k) == 1

    cars = [10, 10, 20, 10, 10]
    k = 20
    assert calc_number_sets_of_cars(cars, k) == 3

    cars = [10, 10]
    k = 20
    assert calc_number_sets_of_cars(cars, k) == 1

    cars = [10, 10]
    k = 21
    assert calc_number_sets_of_cars(cars, k) == 0

    cars = [10]
    k = 21
    assert calc_number_sets_of_cars(cars, k) == 0
