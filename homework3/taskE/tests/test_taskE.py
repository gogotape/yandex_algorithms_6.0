import pytest

from homework3.taskE.taskE import calc_arithmetic_statement, infix_to_postfix


def test_infix_to_postfix():
    infix = "6 + 3 * (1 + 4 * 5) * 2"
    assert infix_to_postfix(infix) == ["6", "3", "1", "4", "5", "*", "+", "*", "2", "*", "+"]

    infix = "8 9 + 1 - 7"
    with pytest.raises(ValueError):
        assert infix_to_postfix(infix) == "8917+*-"

    infix = "1 1 + 2"
    with pytest.raises(ValueError):
        assert infix_to_postfix(infix)

    infix = "10 + 10"
    assert infix_to_postfix(infix) == ["10", "10", "+"]


def test_taskE():
    s = "1+(2*2 - 3)"
    assert calc_arithmetic_statement(s) == "2"

    s = "1+a+1"
    assert calc_arithmetic_statement(s) == "WRONG"

    s = "1 1 + 2"
    assert calc_arithmetic_statement(s) == "WRONG"

    s = "2 + 2"
    assert calc_arithmetic_statement(s) == "4"

    s = "2 * 2"
    assert calc_arithmetic_statement(s) == "4"

    s = "2 - 2"
    assert calc_arithmetic_statement(s) == "0"

    s = "2+2"
    assert calc_arithmetic_statement(s) == "4"

    s = "2 + 2 * (6 - 3)-4"
    assert calc_arithmetic_statement(s) == "4"

    s = "(2 + 5) - (6 * 2"
    assert calc_arithmetic_statement(s) == "WRONG"

    s = "(2 + 5) - (6 * 2)"
    assert calc_arithmetic_statement(s) == "-5"

    s = "(1 + 1) - (6 * 2)"
    assert calc_arithmetic_statement(s) == "-10"

    s = "1+2-3+4-5+6-7+8-9"
    assert calc_arithmetic_statement(s) == "-3"

    s = "1+2-3+4-5+6-7+8-9+10-11+12-13"
    assert calc_arithmetic_statement(s) == "-5"

    s = "10 + 10"
    assert calc_arithmetic_statement(s) == "20"

    s = "(15 + 1) - (6 * 2)"
    assert calc_arithmetic_statement(s) == "4"

    s = "1+2-3+4-5+6-7+8-9+ 1 0 -11+12-13"
    assert calc_arithmetic_statement(s) == "WRONG"
