# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import example as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "hA&n4[v/QNPu"
    int_0 = 2198
    int_1 = 2065
    clock_0 = module_0.Clock(int_0, int_1)
    assert clock_0.hour == 0
    assert clock_0.minute == 25
    clock_0.__sub__(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    bool_1 = True
    clock_0 = module_0.Clock(bool_1, bool_0)
    assert clock_0.hour == 1
    clock_1 = module_0.Clock(bool_1, bool_1)
    assert clock_1.hour == 1
    assert clock_1.minute == 1
    var_0 = clock_0.__add__(bool_0)
    assert var_0.hour == 1
    var_1 = var_0.__str__()
    assert var_1 == "01:00"
    var_2 = var_0.__sub__(bool_0)
    assert var_2.hour == 1
    var_3 = var_2.__str__()
    assert var_3 == "01:00"
    var_4 = var_2.__repr__()
    assert var_4 == "Clock(1, 0)"
    clock_2 = module_0.Clock(bool_1, bool_1)
    assert clock_2.hour == 1
    assert clock_2.minute == 1
    var_5 = clock_2.__str__()
    assert var_5 == "01:01"
    var_5.cleanup()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x1e\x99>S\xc9wSt\x03L\xe2\xac\xc2\xf9l\xeb\xf4\xba\xd6"
    int_0 = 2971
    clock_0 = module_0.Clock(int_0, int_0)
    assert clock_0.hour == 20
    assert clock_0.minute == 31
    var_0 = clock_0.__eq__(int_0)
    assert var_0 is False
    var_1 = var_0.__repr__()
    assert var_1 == "False"
    var_2 = var_0.__eq__(bytes_0)
    var_2.__add__(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -569
    clock_0 = module_0.Clock(int_0, int_0)
    assert clock_0.hour == 21
    assert clock_0.minute == 31
    float_0 = -1725.0009
    module_0.Clock(clock_0, float_0)
