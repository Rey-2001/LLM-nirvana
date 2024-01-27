
import pytest
from validation import Validation

def test_success():
    val = Validation.success(5)
    assert val.value == 5
    assert val.errors == []
    assert val.is_success() is True
    assert val.is_fail() is False

def test_fail():
    val = Validation.fail(["error1", "error2"])
    assert val.value is None
    assert val.errors == ["error1", "error2"]
    assert val.is_success() is False
    assert val.is_fail() is True

def test_eq():
    val1 = Validation.success(5)
    val2 = Validation.success(5)
    val3 = Validation.fail(["error"])
    assert val1 == val2
    assert val1 != val3

def test_map():
    val = Validation.success(5)
    new_val = val.map(lambda x: x * 2)
    assert new_val.value == 10
    assert new_val.errors == []

def test_bind():
    val = Validation.success(5)
    new_val = val.bind(lambda x: Validation.success(x * 2))
    assert new_val.value == 10
    assert new_val.errors == []

def test_ap():
    val1 = Validation.success(5)
    val2 = Validation.success(lambda x: x * 2)
    new_val = val2.ap(val1)
    assert new_val.value(5) == 10
    assert new_val.errors == []

def test_to_either():
    val1 = Validation.success(5)
    val2 = Validation.fail(["error"])
    either1 = val1.to_either()
    either2 = val2.to_either()
    assert either1.is_right() is True
    assert either1.right() == 5
    assert either2.is_left() is True
    assert either2.left() == ["error"]

def test_to_maybe():
    val1 = Validation.success(5)
    val2 = Validation.fail(["error"])
    maybe1 = val1.to_maybe()
    maybe2 = val2.to_maybe()
    assert maybe1.is_just() is True
    assert maybe1.just() == 5
    assert maybe2.is_nothing() is True

def test_to_box():
    val = Validation.success(5)
    box = val.to_box()
    assert box.value == 5

def test_to_lazy():
    val = Validation.success(5)
    lazy = val.to_lazy()
    assert lazy.value() == 5

def test_to_try():
    val1 = Validation.success(5)
    val2 = Validation.fail(["error"])
    try1 = val1.to_try()
    try2 = val2.to_try()
    assert try1.is_success() is True
    assert try1.value == 5
    assert try2.is_success() is False
    assert try2.value == None
