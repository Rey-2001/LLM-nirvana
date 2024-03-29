# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import maybe as module_0


def test_case_0():
    bool_0 = True
    maybe_0 = module_0.Maybe(bool_0, bool_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing is True
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )


def test_case_1():
    none_type_0 = None
    maybe_0 = module_0.Maybe(none_type_0, none_type_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing is None
    assert maybe_0.value is None
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    maybe_0 = module_0.Maybe(bool_0, bool_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing is True
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    none_type_0 = None
    bool_1 = maybe_0.__eq__(none_type_0)
    assert bool_1 is False
    maybe_1 = module_0.Maybe(bool_1, bool_1)
    assert maybe_1.is_nothing is False
    assert maybe_1.value is False
    var_0 = maybe_0.filter(none_type_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "maybe.Maybe"
    assert var_0.is_nothing is True
    maybe_1.filter(var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    maybe_0 = module_0.Maybe(tuple_0, tuple_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing == ()
    assert maybe_0.value == ()
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    bool_0 = True
    maybe_1 = module_0.Maybe(bool_0, bool_0)
    var_0 = maybe_1.map(maybe_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "maybe.Maybe"
    assert var_0.is_nothing is True
    var_0.to_try()


def test_case_4():
    none_type_0 = None
    bool_0 = True
    maybe_0 = module_0.Maybe(none_type_0, bool_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing is True
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    none_type_1 = None
    bool_1 = True
    maybe_1 = module_0.Maybe(bool_1, bool_1)
    var_0 = maybe_1.ap(none_type_1)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "maybe.Maybe"
    assert var_0.is_nothing is True
    var_1 = maybe_1.bind(var_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "maybe.Maybe"
    assert var_1.is_nothing is True
    var_2 = var_0.map(bool_1)
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "maybe.Maybe"
    assert var_2.is_nothing is True
    var_3 = var_2.filter(bool_1)
    assert f"{type(var_3).__module__}.{type(var_3).__qualname__}" == "maybe.Maybe"
    assert var_3.is_nothing is True


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    maybe_0 = module_0.Maybe(none_type_0, none_type_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing is None
    assert maybe_0.value is None
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    maybe_0.bind(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    none_type_0 = None
    bytes_0 = b"x\xcd!30\xd9\xeb\x89lh\xf3\xe5Y\xfe"
    maybe_0 = module_0.Maybe(bytes_0, bytes_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing == b"x\xcd!30\xd9\xeb\x89lh\xf3\xe5Y\xfe"
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    var_0 = maybe_0.ap(none_type_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "maybe.Maybe"
    assert var_0.is_nothing is True
    var_0.to_lazy()


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = True
    none_type_0 = None
    bool_1 = True
    maybe_0 = module_0.Maybe(bool_1, bool_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing is True
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    var_0 = maybe_0.get_or_else(none_type_0)
    bool_2 = maybe_0.__eq__(var_0)
    assert bool_2 is False
    bool_3 = True
    maybe_1 = module_0.Maybe(bool_1, none_type_0)
    assert maybe_1.value is True
    list_0 = [bool_3, bool_0, none_type_0]
    var_1 = maybe_0.filter(list_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "maybe.Maybe"
    assert var_1.is_nothing is True
    bool_4 = var_1.__eq__(maybe_0)
    assert bool_4 is True
    bool_5 = True
    maybe_1.ap(bool_5)


@pytest.mark.xfail(strict=True)
def test_case_8():
    float_0 = -3481.10069
    bytes_0 = b"ZN\xfay\xaf`\xcdV\xa5\x92\xc3\x93P_\x9d\x8fH"
    none_type_0 = None
    maybe_0 = module_0.Maybe(bytes_0, none_type_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing is None
    assert maybe_0.value == b"ZN\xfay\xaf`\xcdV\xa5\x92\xc3\x93P_\x9d\x8fH"
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    maybe_0.filter(float_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    bool_0 = True
    bool_1 = False
    list_0 = [bool_1, bool_1]
    maybe_0 = module_0.Maybe(list_0, list_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing == [False, False]
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    var_0 = maybe_0.get_or_else(bool_0)
    assert var_0 is True
    var_0.to_try()


@pytest.mark.xfail(strict=True)
def test_case_10():
    int_0 = 4549
    none_type_0 = None
    maybe_0 = module_0.Maybe(none_type_0, none_type_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing is None
    assert maybe_0.value is None
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    maybe_1 = module_0.Maybe(maybe_0, none_type_0)
    assert (
        f"{type(maybe_1.value).__module__}.{type(maybe_1.value).__qualname__}"
        == "maybe.Maybe"
    )
    var_0 = maybe_1.get_or_else(int_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "maybe.Maybe"
    assert var_0.is_nothing is None
    assert var_0.value is None
    var_0.to_validation()


@pytest.mark.xfail(strict=True)
def test_case_11():
    bool_0 = False
    bool_1 = False
    maybe_0 = module_0.Maybe(bool_1, bool_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing is False
    assert maybe_0.value is False
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    bool_2 = maybe_0.__eq__(bool_0)
    assert bool_2 is False
    maybe_1 = module_0.Maybe(bool_1, bool_0)
    assert maybe_1.value is False
    maybe_1.map(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    str_0 = 'P9k">^`(a'
    maybe_0 = module_0.Maybe(str_0, str_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing == 'P9k">^`(a'
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    var_0 = maybe_0.filter(str_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "maybe.Maybe"
    assert var_0.is_nothing is True
    bool_0 = var_0.__eq__(var_0)
    assert bool_0 is True
    bool_1 = maybe_0.__eq__(bool_0)
    assert bool_1 is False
    maybe_1 = module_0.Maybe(var_0, bool_1)
    assert maybe_1.is_nothing is False
    assert (
        f"{type(maybe_1.value).__module__}.{type(maybe_1.value).__qualname__}"
        == "maybe.Maybe"
    )
    maybe_1.filter(bool_1)


@pytest.mark.xfail(strict=True)
def test_case_13():
    str_0 = 'P9k">^`(a'
    maybe_0 = module_0.Maybe(str_0, str_0)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing == 'P9k">^`(a'
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    var_0 = maybe_0.filter(str_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "maybe.Maybe"
    assert var_0.is_nothing is True
    bool_0 = maybe_0.ap(var_0)
    assert f"{type(bool_0).__module__}.{type(bool_0).__qualname__}" == "maybe.Maybe"
    assert bool_0.is_nothing is True
    bool_1 = maybe_0.__eq__(bool_0)
    assert bool_1 is False
    maybe_1 = module_0.Maybe(var_0, bool_1)
    assert maybe_1.is_nothing is False
    assert (
        f"{type(maybe_1.value).__module__}.{type(maybe_1.value).__qualname__}"
        == "maybe.Maybe"
    )
    maybe_1.filter(bool_1)


@pytest.mark.xfail(strict=True)
def test_case_14():
    bool_0 = True
    bool_1 = False
    tuple_0 = (bool_1, bool_1)
    list_0 = [tuple_0, bool_1, tuple_0, bool_1]
    none_type_0 = None
    bool_2 = False
    maybe_0 = module_0.Maybe(none_type_0, bool_2)
    assert f"{type(maybe_0).__module__}.{type(maybe_0).__qualname__}" == "maybe.Maybe"
    assert maybe_0.is_nothing is False
    assert maybe_0.value is None
    assert (
        f"{type(module_0.Maybe.just).__module__}.{type(module_0.Maybe.just).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Maybe.nothing).__module__}.{type(module_0.Maybe.nothing).__qualname__}"
        == "builtins.method"
    )
    var_0 = maybe_0.get_or_else(list_0)
    bool_3 = var_0.__eq__(bool_0)
    bool_4 = maybe_0.__eq__(maybe_0)
    assert bool_4 is True
    var_0.ap(tuple_0)
