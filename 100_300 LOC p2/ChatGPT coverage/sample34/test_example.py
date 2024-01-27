import pytest
from google import GoogleParser, Section, SectionType, Docstring, DocstringMeta, DocstringParam, DocstringRaises, DocstringReturns, ParseError

def test_parse_empty():
    parser = GoogleParser()
    docstring = parser.parse('')
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []

def test_parse_short_description_only():
    parser = GoogleParser()
    docstring = parser.parse('This is a short description.')
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description is None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []

def test_parse_long_description_only():
    parser = GoogleParser()
    docstring = parser.parse('\nA long description.\n')
    assert docstring.short_description is None
    assert docstring.long_description == 'A long description.'
    assert docstring.blank_after_short_description == True
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []

def test_parse_short_and_long_description():
    parser = GoogleParser()
    docstring = parser.parse('This is a short description.\n\nA long description.\n')
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'A long description.'
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert docstring.meta == []

def test_parse_multiple_sections():
    parser = GoogleParser()
    docstring_text = '''
    This is a short description.

    Args:
        arg1 (int): Description for arg1.
        arg2 (str): Description for arg2.

    Returns:
        int: Description for the return value.
    '''
    docstring = parser.parse(docstring_text)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description is None
    assert docstring.blank_after_short_description == False
    assert docstring.blank_after_long_description == False
    assert len(docstring.meta) == 3

    assert isinstance(docstring.meta[0], DocstringParam)
    assert docstring.meta[0].args == ['param', 'arg1']
    assert docstring.meta[0].description == 'Description for arg1.'
    assert docstring.meta[0].arg_name == 'arg1'
    assert docstring.meta[0].type_name == 'int'
    assert docstring.meta[0].is_optional == None
    assert docstring.meta[0].default == None

    assert isinstance(docstring.meta[1], DocstringParam)
    assert docstring.meta[1].args == ['param', 'arg2']
    assert docstring.meta[1].description == 'Description for arg2.'
    assert docstring.meta[1].arg_name == 'arg2'
    assert docstring.meta[1].type_name == 'str'
    assert docstring.meta[1].is_optional == None
    assert docstring.meta[1].default == None

    assert isinstance(docstring.meta[2], DocstringReturns)
    assert docstring.meta[2].args == ['returns', 'int']
    assert docstring.meta[2].description == 'Description for the return value.'
    assert docstring.meta[2].type_name == 'int'
    assert docstring.meta[2].is_generator == False