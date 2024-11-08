from homework3.taskA.taskA import is_correct_bracket_sequence


def test_is_correct_bracket_sequence():
    s = "()[]"
    assert is_correct_bracket_sequence(s) == "yes"

    s = "([)]"
    assert is_correct_bracket_sequence(s) == "no"

    s = "("
    assert is_correct_bracket_sequence(s) == "no"
