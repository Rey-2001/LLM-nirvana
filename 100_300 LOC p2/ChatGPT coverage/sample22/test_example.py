
import generation
import pytest
from generation import *

def test_uuid():
    # Test default representation
    uid = generation.uuid()
    assert isinstance(uid, str)
    assert len(uid) == 36
    
    # Test as_hex=True
    uid_hex = generation.uuid(as_hex=True)
    assert isinstance(uid_hex, str)
    assert len(uid_hex) == 32
    assert all(c in '0123456789abcdef' for c in uid_hex)
    
def test_random_string():
    # Test valid size parameter
    size = 10
    rand_str = generation.random_string(size)
    assert isinstance(rand_str, str)
    assert len(rand_str) == size
    
    # Test invalid size parameter
    size = -5
    with pytest.raises(ValueError):
        generation.random_string(size)
    
def test_secure_random_hex():
    # Test valid byte_count parameter
    byte_count = 16
    rand_hex = generation.secure_random_hex(byte_count)
    assert isinstance(rand_hex, str)
    assert len(rand_hex) == 2 * byte_count
    assert all(c in '0123456789abcdef' for c in rand_hex)
    
    # Test invalid byte_count parameter
    byte_count = -5
    with pytest.raises(ValueError):
        generation.secure_random_hex(byte_count)

def test_roman_range():
    # Test ascending range
    for i, roman_numeral in enumerate(generation.roman_range(1, 7)):
        assert isinstance(roman_numeral, str)
        assert roman_numeral == generation.roman_encode(i+1)
    
    # Test descending range
    for i, roman_numeral in enumerate(generation.roman_range(7, 1, -1)):
        assert isinstance(roman_numeral, str)
        assert roman_numeral == generation.roman_encode(7-i)
    
    # Test invalid start parameter
    with pytest.raises(ValueError):
        list(generation.roman_range(1, 7, 0))
    
    # Test invalid stop parameter
    with pytest.raises(ValueError):
        list(generation.roman_range(0))
        list(generation.roman_range(4000))
    
    # Test invalid step parameter
    with pytest.raises(ValueError):
        list(generation.roman_range(1, 7, -1))
