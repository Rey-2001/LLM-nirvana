import keyword
from collections import UserString
from typing import Union
import pytest

from validators import validate_identifier


# Test when identifier ends with underscore
def test_validate_identifier_ends_with_underscore():
    with pytest.raises(SyntaxError):
        validate_identifier('identifier_')


# Test when identifier starts with underscore
def test_validate_identifier_starts_with_underscore():
    with pytest.raises(SyntaxError):
        validate_identifier('_identifier')


# Test when identifier starts with a number
def test_validate_identifier_starts_with_number():
    with pytest.raises(SyntaxError):
        validate_identifier('1identifier')


# Test when identifier is a keyword
def test_validate_identifier_is_keyword():
    with pytest.raises(SyntaxError):
        validate_identifier('for')


# Test when identifier is a builtin name
def test_validate_identifier_is_builtin_name():
    with pytest.raises(SyntaxError):
        validate_identifier('TypeError')


# Test when identifier is an empty string
def test_validate_identifier_empty_string():
    with pytest.raises(SyntaxError):
        validate_identifier('')


# Test when identifier is a valid identifier and does not raise any error
def test_validate_identifier_valid_identifier():
    validate_identifier('validIdentifier')
    validate_identifier('anotherIdentifier')
    validate_identifier('_underscore_var')