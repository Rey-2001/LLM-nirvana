
import pytest
from undefined import *
from undefined import _RaiseUndefinedParameters, _IgnoreUndefinedParameters, _CatchAllUndefinedParameters, UndefinedParameterError, Undefined


def test_UndefinedParameterError():
    with pytest.raises(UndefinedParameterError):
        raise UndefinedParameterError()


def test_RaiseUndefinedParameters_handle_from_dict():
    class TestClass:
        def __init__(self, a):
            self.a = a

    assert _RaiseUndefinedParameters.handle_from_dict(TestClass, {'a': 1}) == {'a': 1}
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(TestClass, {'b': 2})


def test_RaiseUndefinedParameters_create_init():
    class TestClass:
        def __init__(self, a):
            self.a = a

    init_func = _RaiseUndefinedParameters.create_init(TestClass)
    obj = TestClass(1)
    init_func(obj)
    assert obj.a == 1

    with pytest.raises(UndefinedParameterError):
        init_func(obj, b=2)
    assert obj.a == 1


def test_IgnoreUndefinedParameters_handle_from_dict():
    class TestClass:
        def __init__(self, a):
            self.a = a

    assert _IgnoreUndefinedParameters.handle_from_dict(TestClass, {'a': 1}) == {'a': 1}
    assert _IgnoreUndefinedParameters.handle_from_dict(TestClass, {'b': 2}) == {}


def test_IgnoreUndefinedParameters_create_init():
    class TestClass:
        def __init__(self, a):
            self.a = a

    init_func = _IgnoreUndefinedParameters.create_init(TestClass)
    obj = TestClass(1)
    init_func(obj)
    assert obj.a == 1

    init_func(obj, b=2)
    assert obj.a == 1


def test_CatchAllUndefinedParameters_handle_from_dict():
    class TestClass:
        def __init__(self, a, catch_all: CatchAll = None):
            self.a = a
            self.catch_all = catch_all

    assert _CatchAllUndefinedParameters.handle_from_dict(TestClass, {'a': 1}) == {'a': 1}
    assert _CatchAllUndefinedParameters.handle_from_dict(TestClass, {'b': 2}) == {'b': 2}
    assert _CatchAllUndefinedParameters.handle_from_dict(TestClass, {'a': 1, 'b': 2}) == {'a': 1, 'b': 2}


def test_CatchAllUndefinedParameters_create_init():
    class TestClass:
        def __init__(self, a, catch_all: CatchAll = None):
            self.a = a
            self.catch_all = catch_all

    init_func = _CatchAllUndefinedParameters.create_init(TestClass)
    obj = TestClass(1)
    init_func(obj)
    assert obj.a == 1
    assert obj.catch_all is None

    init_func(obj, b=2)
    assert obj.a == 1
    assert obj.catch_all == {'b': 2}

    init_func(obj, b=2, c=3)
    assert obj.a == 1
    assert obj.catch_all == {'b': 2, 'c': 3}


def test_Undefined():
    assert Undefined.INCLUDE.value == _CatchAllUndefinedParameters
    assert Undefined.RAISE.value == _RaiseUndefinedParameters
    assert Undefined.EXCLUDE.value == _IgnoreUndefinedParameters


def test_UndefinedParameterError():
    with pytest.raises(UndefinedParameterError):
        raise UndefinedParameterError()
