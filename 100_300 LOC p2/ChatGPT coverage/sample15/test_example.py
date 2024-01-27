
import pytest

from immutable_list import ImmutableList


def test_constructor():
    lst = ImmutableList(1)
    assert lst.head == 1
    assert lst.tail is None
    assert lst.is_empty is False

def test_constructor_with_empty_list():
    lst = ImmutableList()
    assert lst.head is None
    assert lst.tail is None
    assert lst.is_empty is False

def test_add():
    lst1 = ImmutableList(1, ImmutableList(2))
    lst2 = ImmutableList(3)
    lst3 = lst1 + lst2
    assert lst3.head == 1
    assert lst3.tail.head == 2
    assert lst3.tail.tail.head == 3
    assert lst3.tail.tail.tail is None

def test_add_with_invalid_instance():
    lst1 = ImmutableList(1)
    lst2 = [2, 3]
    with pytest.raises(ValueError):
        lst3 = lst1 + lst2

def test_len():
    lst = ImmutableList(1, ImmutableList(2))
    assert len(lst) == 2

def test_len_with_empty_list():
    lst = ImmutableList()
    assert len(lst) == 0

def test_of():
    lst = ImmutableList.of(1, 2, 3)
    assert lst.head == 1
    assert lst.tail.head == 2
    assert lst.tail.tail.head == 3
    assert lst.tail.tail.tail is None

def test_of_with_single_element():
    lst = ImmutableList.of(1)
    assert lst.head == 1
    assert lst.tail is None

def test_empty():
    lst = ImmutableList.empty()
    assert lst.head is None
    assert lst.tail is None
    assert lst.is_empty is True

def test_to_list():
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert lst.to_list() == [1, 2, 3]

def test_append():
    lst1 = ImmutableList(1, ImmutableList(2))
    lst2 = lst1.append(3)
    assert lst2.head == 1
    assert lst2.tail.head == 2
    assert lst2.tail.tail.head == 3
    assert lst2.tail.tail.tail is None

def test_unshift():
    lst1 = ImmutableList(2, ImmutableList(3))
    lst2 = lst1.unshift(1)
    assert lst2.head == 1
    assert lst2.tail.head == 2
    assert lst2.tail.tail.head == 3
    assert lst2.tail.tail.tail is None

def test_map():
    lst1 = ImmutableList(1, ImmutableList(2))
    lst2 = lst1.map(lambda x: x * 2)
    assert lst2.head == 2
    assert lst2.tail.head == 4
    assert lst2.tail.tail is None

def test_filter():
    lst1 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    lst2 = lst1.filter(lambda x: x % 2 == 0)
    assert lst2.head == 2
    assert lst2.tail is None

def test_find():
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert lst.find(lambda x: x == 2) == 2

def test_find_with_non_existing_element():
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert lst.find(lambda x: x == 4) is None

def test_reduce():
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    result = lst.reduce(lambda acc, x: acc + x, 0)
    assert result == 6
