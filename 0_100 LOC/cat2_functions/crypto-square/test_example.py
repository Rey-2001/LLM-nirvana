# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import example as module_0


def test_case_0():
    str_0 = "|_0;"
    var_0 = module_0.cipher_text(str_0)
    assert var_0 == "0"


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 581
    str_0 = "}Ww'Clcn^cEar8@aa3."
    var_0 = module_0.cipher_text(str_0)
    assert var_0 == "wcaa wnr3 cc8  lea "
    tuple_0 = ()
    tuple_1 = (int_0, str_0, tuple_0)
    module_0.cipher_text(tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.cipher_text(bool_0)
