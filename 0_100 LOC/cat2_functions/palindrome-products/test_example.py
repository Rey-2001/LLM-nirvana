# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import example as module_0


def test_case_0():
    bool_0 = True
    var_0 = module_0.smallest(bool_0, bool_0)


def test_case_1():
    int_0 = -2654
    var_0 = module_0.smallest(int_0, int_0)


def test_case_2():
    bool_0 = True
    var_0 = module_0.largest(bool_0, bool_0)


def test_case_3():
    float_0 = -632.325013
    var_0 = module_0.smallest(float_0, float_0)


def test_case_4():
    int_0 = -2421
    var_0 = module_0.largest(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.num_digits(bool_0)
    assert var_0 == 1
    var_1 = module_0.num_digits(var_0)
    assert var_1 == 1
    float_0 = -632.325013
    module_0.get_extreme_palindrome_with_factors(float_0, var_0, none_type_0)


def test_case_6():
    int_0 = -2654
    var_0 = module_0.largest(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = True
    var_0 = module_0.largest(bool_0, bool_0)
    int_0 = 1972
    int_1 = -126
    bool_1 = True
    module_0.get_extreme_palindrome_with_factors(int_0, int_1, bool_1)


@pytest.mark.xfail(strict=True)
def test_case_8():
    int_0 = 408
    var_0 = module_0.largest(int_0, int_0)
    bool_0 = True
    var_1 = module_0.get_extreme_palindrome_with_factors(bool_0, bool_0, bool_0)
    var_2 = module_0.largest(bool_0, int_0)
    none_type_0 = None
    tuple_0 = ()
    module_0.get_extreme_palindrome_with_factors(none_type_0, tuple_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    int_0 = 408
    int_1 = -531
    var_0 = module_0.largest(int_1, int_0)
    bool_0 = True
    var_1 = module_0.get_extreme_palindrome_with_factors(bool_0, bool_0, bool_0)
    none_type_0 = None
    module_0.smallest(none_type_0, int_0)


def test_case_10():
    int_0 = -2654
    float_0 = -1436.8
    var_0 = module_0.smallest(float_0, int_0)