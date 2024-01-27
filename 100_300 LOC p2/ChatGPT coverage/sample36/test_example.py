
import pytest
from rest import parse, Docstring, DocstringParam, DocstringReturns, DocstringRaises

def test_parse_empty_string():
    text = ""
    result = parse(text)
    assert isinstance(result, Docstring)
    assert result.short_description == None
    assert result.blank_after_short_description == False
    assert result.long_description == None
    assert result.blank_after_long_description == False
    assert result.meta == []

def test_parse_short_description_only():
    text = "This is a short description."
    result = parse(text)
    assert isinstance(result, Docstring)
    assert result.short_description == "This is a short description."
    assert result.blank_after_short_description == False
    assert result.long_description == None
    assert result.blank_after_long_description == False
    assert result.meta == []

def test_parse_short_and_long_description():
    text = "This is a short description.\n\nThis is a long description."
    result = parse(text)
    assert isinstance(result, Docstring)
    assert result.short_description == "This is a short description."
    assert result.blank_after_short_description == False
    assert result.long_description == "This is a long description."
    assert result.blank_after_long_description == False
    assert result.meta == []

def test_parse_meta_param():
    text = ":param arg1: Description of arg1."
    result = parse(text)
    assert isinstance(result, Docstring)
    assert result.short_description == None
    assert result.blank_after_short_description == False
    assert result.long_description == None
    assert result.blank_after_long_description == False
    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringParam)
    assert result.meta[0].args == ["param", "arg1:"]
    assert result.meta[0].description == "Description of arg1."
    assert result.meta[0].arg_name == "arg1"
    assert result.meta[0].type_name == None
    assert result.meta[0].is_optional == None
    assert result.meta[0].default == None

def test_parse_meta_param_with_type():
    text = ":param str arg1: Description of arg1."
    result = parse(text)
    assert isinstance(result, Docstring)
    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringParam)
    assert result.meta[0].args == ["param", "str", "arg1:"]
    assert result.meta[0].description == "Description of arg1."
    assert result.meta[0].arg_name == "arg1"
    assert result.meta[0].type_name == "str"
    assert result.meta[0].is_optional == None
    assert result.meta[0].default == None

def test_parse_meta_param_with_type_and_optional():
    text = ":param str arg1: Description of arg1 (optional)."
    result = parse(text)
    assert isinstance(result, Docstring)
    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringParam)
    assert result.meta[0].args == ["param", "str", "arg1:"]
    assert result.meta[0].description == "Description of arg1 (optional)."
    assert result.meta[0].arg_name == "arg1"
    assert result.meta[0].type_name == "str"
    assert result.meta[0].is_optional == True
    assert result.meta[0].default == None

def test_parse_meta_param_with_type_and_default():
    text = ":param str arg1: Description of arg1 (defaults to 'default')."
    result = parse(text)
    assert isinstance(result, Docstring)
    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringParam)
    assert result.meta[0].args == ["param", "str", "arg1:"]
    assert result.meta[0].description == "Description of arg1 (defaults to 'default')."
    assert result.meta[0].arg_name == "arg1"
    assert result.meta[0].type_name == "str"
    assert result.meta[0].is_optional == False
    assert result.meta[0].default == "'default'"

def test_parse_meta_returns():
    text = ":returns: The result."
    result = parse(text)
    assert isinstance(result, Docstring)
    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringReturns)
    assert result.meta[0].args == ["returns:"]
    assert result.meta[0].description == "The result."
    assert result.meta[0].type_name == None
    assert result.meta[0].is_generator == False

def test_parse_meta_returns_with_type():
    text = ":returns: The result (str)."
    result = parse(text)
    assert isinstance(result, Docstring)
    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringReturns)
    assert result.meta[0].args == ["returns:", "str"]
    assert result.meta[0].description == "The result (str)."
    assert result.meta[0].type_name == "str"
    assert result.meta[0].is_generator == False

def test_parse_meta_yields():
    text = ":yields: The value."
    result = parse(text)
    assert isinstance(result, Docstring)
    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringReturns)
    assert result.meta[0].args == ["yields:"]
    assert result.meta[0].description == "The value."
    assert result.meta[0].type_name == None
    assert result.meta[0].is_generator == True

def test_parse_meta_yields_with_type():
    text = ":yields: The value (int)."
    result = parse(text)
    assert isinstance(result, Docstring)
    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringReturns)
    assert result.meta[0].args == ["yields:", "int"]
    assert result.meta[0].description == "The value (int)."
    assert result.meta[0].type_name == "int"
    assert result.meta[0].is_generator == True

def test_parse_meta_raises():
    text = ":raises: ValueError."
    result = parse(text)
    assert isinstance(result, Docstring)
    assert len(result.meta) == 1
    assert isinstance(result.meta[0], DocstringRaises)
    assert result.meta[0].args == ["raises:", "ValueError"]
    assert result.meta[0].description == "ValueError."
    assert result.meta[0].type_name == "ValueError"


if __name__ == "__main__":
    pytest.main()
