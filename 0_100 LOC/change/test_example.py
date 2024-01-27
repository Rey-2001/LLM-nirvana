# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import example as module_0


def test_case_0():
    int_0 = -1022
    with pytest.raises(ValueError):
        module_0.find_fewest_coins(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 997
    set_0 = {int_0, int_0}
    var_0 = module_0.find_fewest_coins(set_0, int_0)
    module_0.find_fewest_coins(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_fewest_coins(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    none_type_0 = None
    none_type_1 = None
    var_0 = module_0.find_fewest_coins(bool_0, bool_0)
    module_0.find_fewest_coins(none_type_0, none_type_1)


def test_case_4():
    int_0 = 981
    set_0 = {int_0, int_0}
    var_0 = module_0.find_fewest_coins(set_0, int_0)
    int_1 = 2156
    with pytest.raises(ValueError):
        module_0.find_fewest_coins(var_0, int_1)


def test_case_5():
    int_0 = 997
    set_0 = {int_0, int_0}
    var_0 = module_0.find_fewest_coins(set_0, int_0)
    var_1 = module_0.find_fewest_coins(var_0, int_0)
    bytes_0 = b"\xa2\xf2IA\xaf\x8e\xaa\xde\xe0\xecJ"
    var_2 = module_0.find_fewest_coins(bytes_0, int_0)