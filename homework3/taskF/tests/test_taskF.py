from homework3.taskF.taskF import find_lexical_min_correct_bracket_sequence


def test_find_lexical_min_correct_bracket_sequence_example_1():
    n = 6
    w = "()[]"
    s = "([("
    assert find_lexical_min_correct_bracket_sequence(n, w, s) == "([()])"


def test_find_lexical_min_correct_bracket_sequence_example_2():
    n = 6
    w = "][)("
    s = "(["
    assert find_lexical_min_correct_bracket_sequence(n, w, s) == "([][])"


def test_find_lexical_min_correct_bracket_sequence_example_3():
    n = 4
    w = "(][)"
    s = "()[]"
    assert find_lexical_min_correct_bracket_sequence(n, w, s) == "()[]"


def test_find_lexical_min_correct_bracket_sequence_example_4():
    n = 6
    w = "])(["
    s = ""
    assert find_lexical_min_correct_bracket_sequence(n, w, s) == "()()()"


def test_find_lexical_min_correct_bracket_sequence_example_5():
    n = 10
    w = "][()"
    s = "([]("
    answer = "([]([][]))"
    assert find_lexical_min_correct_bracket_sequence(n, w, s) == answer
