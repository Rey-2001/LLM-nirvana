
import decimal
import re
import typing
from math import isfinite

import pytest

# Import the module to be tested
from fields import *


def test_string_field_validate_blank():
    field = String(allow_blank=True)
    assert field.validate("") == ""
    assert field.validate(" ") == " "
    assert field.validate("abc") == "abc"

def test_string_field_validate_not_blank():
    field = String(allow_blank=False)
    assert field.validate("") == ValidationError
    assert field.validate(" ") == " "
    assert field.validate("abc") == "abc"

def test_string_field_validate_pattern():
    field = String(pattern=r"^([a-z]+)$")
    assert field.validate("abc") == "abc"
    assert field.validate("ABC") == ValidationError

def test_string_field_serialize():
    field = String()
    assert field.serialize("abc") == "abc"

def test_number_field_validate_integer():
    field = Number()
    assert field.validate(10) == 10
    assert field.validate(10.0) == 10.0
    assert field.validate("10") == 10
    assert field.validate("10.0") == 10.0

def test_number_field_validate_decimal():
    field = Number()
    assert field.validate(decimal.Decimal(10)) == decimal.Decimal(10)
    assert field.validate(decimal.Decimal("10.0")) == decimal.Decimal(10.0)

def test_boolean_field_validate():
    field = Boolean()
    assert field.validate(True) == True
    assert field.validate(False) == False
    assert field.validate("true") == True
    assert field.validate("false") == False
    assert field.validate("on") == True
    assert field.validate("off") == False
    assert field.validate("1") == True
    assert field.validate("0") == False
    assert field.validate("") == False
    assert field.validate(1) == True
    assert field.validate(0) == False
    assert field.validate(None) == ValidationError

def test_choice_field_validate():
    field = Choice(choices=["option1", "option2"])
    assert field.validate("option1") == "option1"
    assert field.validate("option2") == "option2"
    assert field.validate("option3") == ValidationError

def test_choice_field_validate_with_tuples():
    field = Choice(choices=[("option1", "Option 1"), ("option2", "Option 2")])
    assert field.validate("option1") == "option1"
    assert field.validate("option2") == "option2"
    assert field.validate("option3") == ValidationError

def test_object_field_validate():
    field = Object(properties={"field1": String(), "field2": Integer()})
    assert field.validate({"field1": "abc", "field2": 10}) == {"field1": "abc", "field2": 10}
    assert field.validate({"field1": "abc", "field2": 10, "field3": "def"}) == {"field1": "abc", "field2": 10, "field3": "def"}
    assert field.validate({"field1": "abc"}) == ValidationError

def test_array_field_validate():
    field = Array(items=String())
    assert field.validate(["abc", "def"]) == ["abc", "def"]
    assert field.validate(["abc", 123]) == ValidationError
    assert field.validate([]) == []

def test_text_field_validate():
    field = Text()
    assert field.validate("abc") == "abc"
    assert field.validate("123") == "123"
    assert field.validate(123) == ValidationError

def test_union_field_validate():
    field = Union(any_of=[String(), Integer()])
    assert field.validate("abc") == "abc"
    assert field.validate(123) == 123
    assert field.validate(10.0) == ValidationError

def test_const_field_validate():
    field = Const(const="abc")
    assert field.validate("abc") == "abc"
    assert field.validate("def") == ValidationError
    assert field.validate(123) == ValidationError

def test_any_field_validate():
    field = Any()
    assert field.validate("abc") == "abc"
    assert field.validate(123) == 123
    assert field.validate(True) == True
    assert field.validate(None) == None

