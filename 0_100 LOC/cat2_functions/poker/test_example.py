# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import example as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"L4\xc8@)j\xb8\x1bF\xeeM\x98n"
    module_0.best_hands(bytes_0)


def test_case_1():
    set_0 = set()
    var_0 = module_0.allmax(set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.best_hands(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    module_0.allmax(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "P*"
    module_0.hand_rank(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    module_0.hand_rank(none_type_0)


def test_case_6():
    bytes_0 = b"L4\xc8@)j\xb8\x1bF\xeeM\x98n"
    var_0 = module_0.allmax(bytes_0)


def test_case_7():
    int_0 = -3752
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.allmax(list_0)


def test_case_8():
    str_0 = "\x0b4/"
    var_0 = module_0.hand_rank(str_0)


def test_case_9():
    str_0 = "Jv\x0b4/"
    var_0 = module_0.hand_rank(str_0)
