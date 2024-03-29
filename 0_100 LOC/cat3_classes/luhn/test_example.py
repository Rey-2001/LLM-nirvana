# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import example as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "5`(ee*RT=2\t~Ne%`3KvO"
    luhn_0 = module_0.Luhn(str_0)
    assert f"{type(luhn_0).__module__}.{type(luhn_0).__qualname__}" == "example.Luhn"
    assert luhn_0.card_num == "5`(ee*RT=2\t~Ne%`3KvO"
    assert luhn_0.checksum == -1
    var_0 = luhn_0.valid()
    assert var_0 is False
    var_1 = luhn_0.valid()
    assert var_1 is False
    float_0 = -356.101728
    module_0.Luhn(float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.Luhn(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "48"
    luhn_0 = module_0.Luhn(str_0)
    assert f"{type(luhn_0).__module__}.{type(luhn_0).__qualname__}" == "example.Luhn"
    assert luhn_0.card_num == "48"
    assert luhn_0.checksum == 16
    var_0 = luhn_0.valid()
    assert var_0 is False
    var_0.valid()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "4"
    luhn_0 = module_0.Luhn(str_0)
    assert luhn_0.checksum == -1
    float_0 = -356.101728
    var_0 = luhn_0.valid()
    assert var_0 is False
    module_0.Luhn(float_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "81"
    luhn_0 = module_0.Luhn(str_0)
    assert f"{type(luhn_0).__module__}.{type(luhn_0).__qualname__}" == "example.Luhn"
    assert luhn_0.card_num == "81"
    assert luhn_0.checksum == 8
    var_0 = luhn_0.valid()
    assert var_0 is False
    var_0.valid()
