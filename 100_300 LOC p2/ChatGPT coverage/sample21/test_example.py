import pytest
from functools import reduce
from typing import List, Any
from utils import curry, eq, increase, identity, curried_map, curried_filter, find, compose, pipe, cond, memoize

def test_curry():
	assert curry(increase)(3)==4
	
def test_eq():
	assert eq(2)(2)==True

def test_curried_map():
	assert curried_map(increase, [1, 2, 3])==[2, 3, 4]

def test_curried_filter():
	assert curried_filter(eq(2), [1, 2, 3, 2]) == [2,2]

def test_find():
	assert find([1,2,3,4,5], eq(3))==3

def test_compose():
	assert compose(2, increase, increase)==4

def test_pipe():
	assert pipe(2, increase, increase) == 4
	
def test_cond():
	assert cond([(eq(2),increase)]) == 3

def test_memoize():
	increase_memoized = memoize(increase)
	assert increase_memoized(2)==3