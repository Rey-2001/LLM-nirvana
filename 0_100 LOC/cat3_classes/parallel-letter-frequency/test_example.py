# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import example as module_0


def test_case_0():
    dict_0 = {}
    var_0 = module_0.calculate(dict_0)
    assert module_0.TOTAL_WORKERS == 3


def test_case_1():
    letter_counter_0 = module_0.LetterCounter()
    assert module_0.TOTAL_WORKERS == 3


@pytest.mark.xfail(strict=True)
def test_case_2():
    letter_counter_0 = module_0.LetterCounter()
    assert module_0.TOTAL_WORKERS == 3
    letter_counter_0.add_counter(letter_counter_0)
