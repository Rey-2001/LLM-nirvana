
import pytest
from numpydoc import NumpydocParser

def test_parse_empty_string():
    parser = NumpydocParser()
    docstring = parser.parse("")
    
    assert docstring == Docstring()

def test_parse_short_description():
    parser = NumpydocParser()
    docstring = parser.parse("Short description")
    
    assert docstring.short_description == "Short description"
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False

def test_parse_long_description():
    parser = NumpydocParser()
    docstring = parser.parse("Short description\n\nLong description")
    
    assert docstring.short_description == "Short description"
    assert docstring.long_description == "Long description"
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False

def test_parse_multiple_sections():
    parser = NumpydocParser()
    docstring = parser.parse("Short description\n\nLong description\n\nParameters\n----------\nparam1 : type\n    Description of param1\n\nReturns\n-------\nreturn_type\n    Description of return value")
    
    assert docstring.short_description == "Short description"
    assert docstring.long_description == "Long description"
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False
    
    assert len(docstring.meta) == 2
    
    param_section = docstring.meta[0]
    assert param_section.key == "param"
    assert len(param_section.args) == 1
    assert param_section.args[0] == "Parameters"
    assert len(param_section.args) == 2
    assert param_section.args[1] == "param1"
    assert param_section.description == "Description of param1"
    
    returns_section = docstring.meta[1]
    assert returns_section.key == "returns"
    assert len(returns_section.args) == 1
    assert returns_section.args[0] == "Returns"
    assert returns_section.description == "Description of return value"
