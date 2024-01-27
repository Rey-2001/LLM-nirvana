import pytest
from semigroups import Sum, All, One, First, Last, Map, Max, Min

# Test cases for Sum
def test_sum_init():
    s = Sum(5)
    assert s.value == 5

def test_sum_eq():
    s1 = Sum(5)
    s2 = Sum(5)
    assert s1 == s2

def test_sum_fold():
    s = Sum(5)
    assert s.fold(lambda x: x * 2) == 10

def test_sum_concat():
    s1 = Sum(5)
    s2 = Sum(3)
    assert s1.concat(s2) == Sum(8)

# Test cases for All
def test_all_init():
    a = All(True)
    assert a.value == True

def test_all_eq():
    a1 = All(True)
    a2 = All(True)
    assert a1 == a2

def test_all_fold():
    a = All(True)
    assert a.fold(lambda x: not x) == False

def test_all_concat_true_true():
    a1 = All(True)
    a2 = All(True)
    assert a1.concat(a2) == All(True)

def test_all_concat_true_false():
    a1 = All(True)
    a2 = All(False)
    assert a1.concat(a2) == All(False)

# Test cases for One
def test_one_init():
    o = One(True)
    assert o.value == True

def test_one_eq():
    o1 = One(True)
    o2 = One(True)
    assert o1 == o2

def test_one_fold():
    o = One(True)
    assert o.fold(lambda x: not x) == False

def test_one_concat_true_true():
    o1 = One(True)
    o2 = One(True)
    assert o1.concat(o2) == One(True)

def test_one_concat_true_false():
    o1 = One(True)
    o2 = One(False)
    assert o1.concat(o2) == One(True)

# Test cases for First
def test_first_init():
    f = First("abc")
    assert f.value == "abc"

def test_first_eq():
    f1 = First("abc")
    f2 = First("abc")
    assert f1 == f2

def test_first_fold():
    f = First("abc")
    assert f.fold(lambda x: x.upper()) == "ABC"

def test_first_concat():
    f1 = First("abc")
    f2 = First("def")
    assert f1.concat(f2) == First("abc")

# Test cases for Last
def test_last_init():
    l = Last("abc")
    assert l.value == "abc"

def test_last_eq():
    l1 = Last("abc")
    l2 = Last("abc")
    assert l1 == l2

def test_last_fold():
    l = Last("abc")
    assert l.fold(lambda x: x.upper()) == "ABC"

def test_last_concat():
    l1 = Last("abc")
    l2 = Last("def")
    assert l1.concat(l2) == Last("def")

# Test cases for Map
def test_map_init():
    m = Map({1: Sum(5), 2: Sum(3)})
    assert m.value == {1: Sum(5), 2: Sum(3)}

def test_map_eq():
    m1 = Map({1: Sum(5), 2: Sum(3)})
    m2 = Map({1: Sum(5), 2: Sum(3)})
    assert m1 == m2

def test_map_fold():
    m = Map({1: Sum(5), 2: Sum(3)})
    assert m.fold(lambda x: sum([v.value for v in x.values()])) == 8

def test_map_concat():
    m1 = Map({1: Sum(5), 2: Sum(3)})
    m2 = Map({2: Sum(7), 3: Sum(2)})
    assert m1.concat(m2) == Map({1: Sum(5), 2: Sum(10), 3: Sum(2)})

# Test cases for Max
def test_max_init():
    mx = Max(5)
    assert mx.value == 5

def test_max_eq():
    mx1 = Max(5)
    mx2 = Max(5)
    assert mx1 == mx2

def test_max_fold():
    mx = Max(5)
    assert mx.fold(lambda x: x * 2) == 10

def test_max_concat():
    mx1 = Max(5)
    mx2 = Max(3)
    assert mx1.concat(mx2) == Max(5)

# Test cases for Min
def test_min_init():
    mn = Min(5)
    assert mn.value == 5

def test_min_eq():
    mn1 = Min(5)
    mn2 = Min(5)
    assert mn1 == mn2

def test_min_fold():
    mn = Min(5)
    assert mn.fold(lambda x: x * 2) == 10

def test_min_concat():
    mn1 = Min(5)
    mn2 = Min(3)
    assert mn1.concat(mn2) == Min(3)