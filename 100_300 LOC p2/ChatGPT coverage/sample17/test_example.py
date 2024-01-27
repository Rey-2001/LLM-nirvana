
import pytest
from maybe import Maybe
from maybe import Box, Lazy, Try, Validation, Either

def test_just():
    m = Maybe.just(5)
    assert not m.is_nothing
    assert m.value == 5

def test_nothing():
    m = Maybe.nothing()
    assert m.is_nothing
    assert m.value == None

def test_map_just():
    m = Maybe.just(5)
    result = m.map(lambda x: x * 2)
    assert not result.is_nothing
    assert result.value == 10

def test_map_nothing():
    m = Maybe.nothing()
    result = m.map(lambda x: x * 2)
    assert result.is_nothing
    assert result.value == None

def test_bind_just():
    m = Maybe.just(5)
    result = m.bind(lambda x: Maybe.just(x * 2))
    assert not result.is_nothing
    assert result.value == 10

def test_bind_nothing():
    m = Maybe.nothing()
    result = m.bind(lambda x: Maybe.just(x * 2))
    assert result.is_nothing
    assert result.value == None

def test_ap_just():
    m1 = Maybe.just(lambda x: x * 2)
    m2 = Maybe.just(5)
    result = m1.ap(m2)
    assert not result.is_nothing
    assert result.value == 10

def test_ap_nothing():
    m1 = Maybe.just(lambda x: x * 2)
    m2 = Maybe.nothing()
    result = m1.ap(m2)
    assert result.is_nothing
    assert result.value == None

def test_filter_just_pass():
    m = Maybe.just(5)
    result = m.filter(lambda x: x >= 5)
    assert not result.is_nothing
    assert result.value == 5

def test_filter_just_fail():
    m = Maybe.just(5)
    result = m.filter(lambda x: x < 5)
    assert result.is_nothing
    assert result.value == None

def test_filter_nothing():
    m = Maybe.nothing()
    result = m.filter(lambda x: x >= 5)
    assert result.is_nothing
    assert result.value == None

def test_get_or_else_just():
    m = Maybe.just(5)
    result = m.get_or_else(0)
    assert result == 5

def test_get_or_else_nothing():
    m = Maybe.nothing()
    result = m.get_or_else(0)
    assert result == 0

def test_to_either_just():
    m = Maybe.just(5)
    result = m.to_either()
    assert isinstance(result, Either)
    assert result.is_right
    assert result.value == 5

def test_to_either_nothing():
    m = Maybe.nothing()
    result = m.to_either()
    assert isinstance(result, Either)
    assert result.is_left
    assert result.value == None

def test_to_box_just():
    m = Maybe.just(5)
    result = m.to_box()
    assert isinstance(result, Box)
    assert result.value == 5

def test_to_box_nothing():
    m = Maybe.nothing()
    result = m.to_box()
    assert isinstance(result, Box)
    assert result.value == None

def test_to_lazy_just():
    m = Maybe.just(5)
    result = m.to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() == 5

def test_to_lazy_nothing():
    m = Maybe.nothing()
    result = m.to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() == None

def test_to_try_just():
    m = Maybe.just(5)
    result = m.to_try()
    assert isinstance(result, Try)
    assert result.is_success
    assert result.value == 5

def test_to_try_nothing():
    m = Maybe.nothing()
    result = m.to_try()
    assert isinstance(result, Try)
    assert not result.is_success
    assert result.value == None

def test_to_validation_just():
    m = Maybe.just(5)
    result = m.to_validation()
    assert isinstance(result, Validation)
    assert result.is_success
    assert result.value == 5

def test_to_validation_nothing():
    m = Maybe.nothing()
    result = m.to_validation()
    assert isinstance(result, Validation)
    assert result.is_success
    assert result.value == None
