
import pytest
from box import Box

def test_box_init():
    value = 5
    box = Box(value)
    assert box.value == value

def test_box_eq():
    value1 = 5
    value2 = 5
    box1 = Box(value1)
    box2 = Box(value2)
    assert box1 == box2

def test_box_str():
    value = 5
    box = Box(value)
    assert str(box) == 'Box[value=5]'

def test_box_map():
    value = 5
    box = Box(value)
    mapper = lambda x: x + 5
    mapped_box = box.map(mapper)
    assert mapped_box.value == value + 5

def test_box_bind():
    value = 5
    box = Box(value)
    mapper = lambda x: x + 5
    mapped_value = box.bind(mapper)
    assert mapped_value == value + 5

def test_box_ap():
    value1 = 5
    value2 = lambda x: x+5
    box1 = Box(value1)
    box2 = Box(value2)
    new_box = box1.ap(box2)
    assert new_box.value(10) == 15

def test_box_to_maybe():
    value = 5
    box = Box(value)
    maybe = box.to_maybe()
    assert maybe.is_just() == True
    assert maybe.get() == value

def test_box_to_either():
    value = 5
    box = Box(value)
    either = box.to_either()
    assert either.is_right() == True
    assert either.get() == value

def test_box_to_lazy():
    value = 5
    box = Box(value)
    lazy = box.to_lazy()
    assert lazy.evaluate() == value

def test_box_to_try():
    value = 5
    box = Box(value)
    try_monad = box.to_try()
    assert try_monad.is_success() == True
    assert try_monad.get() == value

def test_box_to_validation():
    value = 5
    box = Box(value)
    validation = box.to_validation()
    assert validation.is_success() == True
    assert validation.get() == value

