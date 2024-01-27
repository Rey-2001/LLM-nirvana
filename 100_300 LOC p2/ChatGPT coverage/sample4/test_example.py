
import strutils
from strutils import *

def test_as_escaped_unicode_literal():
    text = '1.★ 🛑'
    expected_output = r'\x31\x2e\xE2\x98\x85\x20\xF0\x9F\x9B\x91'
    assert strutils.as_escaped_unicode_literal(text) == expected_output

def test_as_escaped_utf8_literal():
    text = '1.★ 🛑'
    expected_output = r'\x31\x2e\xE2\x98\x85\x20\xF0\x9F\x9B\x91'
    assert strutils.as_escaped_utf8_literal(text) == expected_output

def test_camel_to_underscore():
    text = 'FooBar'
    expected_output = 'foo_bar'
    assert strutils.camel_to_underscore(text) == expected_output

def test_convert_escaped_unicode_literal():
    text = r'\x31\x2e\xE2\x98\x85\x20\xF0\x9F\x9B\x91'
    expected_output = '1.★ 🛑'
    assert strutils.convert_escaped_unicode_literal(text) == expected_output

def test_convert_escaped_utf8_literal():
    text = r'\x31\x2e\xE2\x98\x85\x20\xF0\x9F\x9B\x91'
    expected_output = '1.★ 🛑'
    assert strutils.convert_escaped_utf8_literal(text) == expected_output

def test_underscore_to_camel():
    text = 'foo_bar'
    expected_output = 'fooBar'
    assert strutils.underscore_to_camel(text) == expected_output

    text = '_one__two___'
    expected_output = 'oneTwo'
    assert strutils.underscore_to_camel(text, lower_first=False) == expected_output
