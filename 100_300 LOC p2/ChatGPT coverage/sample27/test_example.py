import pytest
from json_schema import from_json_schema, to_json_schema
from json_schema import *

def test_from_json_schema():
    data = {
        "type": "string",
        "minLength": 5,
        "maxLength": 10,
        "default": "default_value"
    }
    field = from_json_schema(data)
    assert isinstance(field, String)
    assert field.min_length == 5
    assert field.max_length == 10
    assert field.default == "default_value"


def test_to_json_schema():
    field = String(min_length=5, max_length=10, default="default_value")
    json_schema = to_json_schema(field)
    assert json_schema == {
        "type": "string",
        "minLength": 5,
        "maxLength": 10,
        "default": "default_value"
    }