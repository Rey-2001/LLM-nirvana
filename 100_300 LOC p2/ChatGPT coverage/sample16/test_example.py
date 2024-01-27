
import pytest
from lazy import Lazy

def test_lazy_of():
    lazy = Lazy.of(5)
    assert lazy.get() == 5

def test_lazy_with_map():
    lazy = Lazy.of(5)
    lazy_map = lazy.map(lambda x: x + 5)
    assert lazy_map.get() == 10

def test_lazy_with_ap():
    lazy1 = Lazy.of(lambda x: x + 5)
    lazy2 = Lazy.of(5)
    lazy_ap = lazy1.ap(lazy2)
    assert lazy_ap.get() == 10

def test_lazy_with_bind():
    lazy = Lazy.of(5)
    lazy_bind = lazy.bind(lambda x: Lazy.of(x + 5))
    assert lazy_bind.get() == 10

def test_lazy_with_to_box():
    lazy = Lazy.of(5)
    box = lazy.to_box()
    assert box.get() == 5

def test_lazy_with_to_either():
    lazy = Lazy.of(5)
    either = lazy.to_either()
    assert either.get() == 5

def test_lazy_with_to_maybe():
    lazy = Lazy.of(5)
    maybe = lazy.to_maybe()
    assert maybe.get() == 5

def test_lazy_with_to_try():
    lazy = Lazy.of(5)
    try_ = lazy.to_try()
    assert try_.get() == 5

def test_lazy_with_to_validation():
    lazy = Lazy.of(5)
    validation = lazy.to_validation()
    assert validation.get() == 5
