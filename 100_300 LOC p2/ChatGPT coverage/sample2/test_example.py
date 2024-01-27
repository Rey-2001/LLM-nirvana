
import pytest
from objutils import (has_any_attrs, has_any_callables, has_attrs, has_callables, is_list_like, is_subclass_of_any)
from objutils import *
# has_any_attrs
def test_has_any_attrs_returns_true_when_object_has_any_attributes():
    obj = {'a': 1, 'b': 2}
    assert has_any_attrs(obj, 'keys', 'values', 'items') is True

def test_has_any_attrs_returns_false_when_object_does_not_have_any_attributes():
    obj = {'a': 1, 'b': 2}
    assert has_any_attrs(obj, 'foo', 'bar', 'baz') is False

# has_any_callables
def test_has_any_callables_returns_true_when_object_has_any_callable_attributes():
    obj = {'a': 1, 'b': 2}
    assert has_any_callables(obj, 'keys', 'values', 'items') is True

def test_has_any_callables_returns_false_when_object_does_not_have_any_callable_attributes():
    obj = {'a': 1, 'b': 2}
    assert has_any_callables(obj, 'foo', 'bar', 'baz') is False

# has_attrs
def test_has_attrs_returns_true_when_object_has_all_attributes():
    obj = {'a': 1, 'b': 2}
    assert has_attrs(obj, 'keys', 'values', 'items') is True

def test_has_attrs_returns_false_when_object_does_not_have_all_attributes():
    obj = {'a': 1, 'b': 2}
    assert has_attrs(obj, 'keys', 'values', 'foo') is False

# has_callables
def test_has_callables_returns_true_when_object_has_all_callable_attributes():
    obj = {'a': 1, 'b': 2}
    assert has_callables(obj, 'keys', 'values', 'items') is True

def test_has_callables_returns_false_when_object_does_not_have_all_callable_attributes():
    obj = {'a': 1, 'b': 2}
    assert has_callables(obj, 'keys', 'values', 'foo') is False

# is_list_like
def test_is_list_like_returns_true_when_object_is_list_like():
    obj = [1, 2, 3]
    assert is_list_like(obj) is True

def test_is_list_like_returns_false_when_object_is_not_list_like():
    obj = 'hello'
    assert is_list_like(obj) is False

# is_subclass_of_any
def test_is_subclass_of_any_returns_true_when_object_is_subclass_of_any_classes():
    obj = {'a': 1, 'b': 2}
    assert is_subclass_of_any(obj.keys(), list, set, dict) is True

def test_is_subclass_of_any_returns_false_when_object_is_not_subclass_of_any_classes():
    obj = {'a': 1, 'b': 2}
    assert is_subclass_of_any(obj.keys(), tuple, deque, str) is False
