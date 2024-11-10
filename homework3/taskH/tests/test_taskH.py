from homework3.taskH.taskH import StackWithTopSum


def test_stack_top_3():
    stack = StackWithTopSum()
    assert stack.sum_top_elements(0) == 0
    stack.add(1)
    assert stack.sum_top_elements(1) == 1
    stack.add(2)
    stack.add(3)
    assert stack.sum_top_elements(3) == 6
    stack.add(4)
    assert stack.sum_top_elements(3) == 9
    assert stack.pop() == 4
    assert stack.sum_top_elements(3) == 6
    stack.pop()
    assert stack.sum_top_elements(2) == 3
    assert stack.pop() == 2
    assert stack.sum_top_elements(1) == 1
    assert stack.pop() == 1
    assert stack.sum_top_elements(0) == 0


def test_example_stack():
    stack = StackWithTopSum()
    stack.add(1)
    stack.add(2)
    stack.add(3)
    assert stack.sum == 6

    assert stack.sum_top_elements(2) == 5

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.sum_top_elements(1) == 1


def test_process_operations():
    stack = StackWithTopSum()
    operations = ["+1", "+2", "+3", "?2", "-", "-", "?1"]
    assert stack.process_operations(operations) == [5, 3, 2, 1]
