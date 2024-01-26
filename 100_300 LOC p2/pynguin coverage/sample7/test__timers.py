# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import _timers as module_0


def test_case_0():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    str_0 = "(l\\X&s"
    timers_0.mean(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    none_type_0 = None
    timers_0.count(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    str_0 = "9gbB-T@\t)3"
    bool_0 = False
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.mean(str_0)
    assert float_0 == 0
    timers_0.total(float_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    none_type_0 = timers_0.clear()
    timers_0.min(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    str_0 = "Y\r.Q@Pf"
    timers_0.max(str_0)


def test_case_6():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    str_0 = "9gbB-T@\t)3"
    bool_0 = False
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.median(str_0)
    assert float_0 is False


def test_case_7():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    str_0 = "'gbB-TI\t)3"
    bool_0 = False
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.min(str_0)
    assert float_0 is False


def test_case_8():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    str_0 = "A0Nnw< uw/Mi>"
    bool_0 = False
    with pytest.raises(TypeError):
        timers_0.__setitem__(str_0, bool_0)


def test_case_9():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    str_0 = "9bB-T@\t)"
    with pytest.raises(KeyError):
        timers_0.stdev(str_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    str_0 = "9gbB-T@\t)3"
    bool_0 = False
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.mean(str_0)
    assert float_0 == 0
    float_1 = timers_0.stdev(str_0)
    timers_0.total(float_0)


def test_case_11():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    str_0 = "'gbB-TI\t)3"
    bool_0 = False
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.max(str_0)
    assert float_0 is False


@pytest.mark.xfail(strict=True)
def test_case_12():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    str_0 = "9bB-T@\t)3"
    bool_0 = True
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.stdev(str_0)
    float_1 = timers_0.max(str_0)
    assert float_1 is True
    var_0 = timers_0.keys()
    none_type_1 = timers_0.add(str_0, float_1)
    float_2 = timers_0.stdev(str_0)
    assert float_2 == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_1 = timers_0.keys()
    var_1.apply(var_1, float_1)


def test_case_13():
    timers_0 = module_0.Timers()
    assert len(timers_0) == 0
    str_0 = "9gbB-T@\t)3"
    bool_0 = False
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.mean(str_0)
    assert float_0 == 0