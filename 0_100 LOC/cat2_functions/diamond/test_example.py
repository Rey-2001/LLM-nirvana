# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import example as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.make_half(bool_0, bool_0)
    module_0.make_half(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    module_0.rows(dict_0)
