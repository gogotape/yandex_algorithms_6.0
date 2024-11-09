from homework3.taskD.taskD import calc_postfix_statement


def test_taskD():
    s = "8 9 + 1 7 - *"
    assert calc_postfix_statement(s) == -102

    s = "8 9 + 1 7 - *     "
    assert calc_postfix_statement(s) == -102

    s = "89+17-*"
    assert calc_postfix_statement(s) == -102

    s = "1 2 + 4 * 3 +"
    assert calc_postfix_statement(s) == 15

    s = "2 3 *    "
    assert calc_postfix_statement(s) == 6

    s = "2 3 -    "
    assert calc_postfix_statement(s) == -1

    s = "2 3 +    "
    assert calc_postfix_statement(s) == 5
