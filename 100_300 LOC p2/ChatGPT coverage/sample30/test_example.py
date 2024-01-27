
import pytest
from tokenize_yaml import tokenize_yaml, validate_yaml, ValidationError, ParseError, Position

@pytest.mark.parametrize("content, expected_error", [
    ("", "No content."),
    ("Not a valid YAML string", "parse_error")
])
def test_tokenize_yaml_error(content, expected_error):
    with pytest.raises(ParseError) as exc:
        tokenize_yaml(content)
    assert exc.value.text == expected_error

def test_tokenize_yaml():
    content = '''
    name: John Doe
    age: 25
    '''

    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.start == 1
    assert token.end == 25
    assert token.content == content.strip()

@pytest.mark.parametrize("content, validator, expected_value, expected_errors", [
    ("name: John\nage: 25", {"name": str, "age": int}, {"name": "John", "age": 25}, []),
    ("name: John\nage: 25", {"name": str, "age": str}, None, ["age must be of type str"]),
    ("name: John\nage: abc", {"name": str, "age": int}, None, ["age must be of type int"]),
])
def test_validate_yaml(content, validator, expected_value, expected_errors):
    value, errors = validate_yaml(content, validator)
    assert value == expected_value
    assert errors == expected_errors

def test_validate_yaml_empty_string():
    with pytest.raises(ParseError) as exc:
        validate_yaml("", {"name": str, "age": int})
    assert exc.value.text == "No content."
    assert exc.value.code == "no_content"
    assert exc.value.position == Position(line_no=1, column_no=1, char_index=0)

def test_validate_yaml_parse_error():
    with pytest.raises(ParseError) as exc:
        validate_yaml("Not a valid YAML string", {"name": str, "age": int})
    assert exc.value.text == "parse_error"
    assert exc.value.code == "parse_error"
    assert exc.value.position == Position(line_no=1, column_no=1, char_index=0)
