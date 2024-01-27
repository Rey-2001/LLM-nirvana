import pytest

from tokens import Token, ScalarToken, DictToken, ListToken

def test_token_string():
    t = Token("string", 0, 5, "tokens")
    assert t.string == "exampl"

def test_token_value():
    t = Token("value", 0, 4, "tokens")
    assert t.value == "value"

def test_token_start():
    t = Token("start", 0, 4, "tokens")
    assert t.start.line == 1
    assert t.start.column == 1
    assert t.start.offset == 0

def test_token_end():
    t = Token("end", 0, 2, "tokens")
    assert t.end.line == 1
    assert t.end.column == 3
    assert t.end.offset == 2

def test_token_lookup():
    d1 = DictToken({"key1": ScalarToken("value1", 0, 5, "tokens")}, 0, 5, "tokens")
    t = d1.lookup(["key1"])
    assert t.value == "value1"

def test_token_lookup_key():
    d1 = DictToken({"key1": ScalarToken("value1", 0, 5, "tokens")}, 0, 5, "tokens")
    t = d1.lookup_key(["key1"])
    assert t.value == "key1"

def test_scalar_token_get_value():
    s = ScalarToken("value", 0, 4, "tokens")
    assert s._get_value() == "value"

def test_dict_token_get_value():
    d = DictToken({"key": ScalarToken("value", 0, 4, "tokens")}, 0, 4, "tokens")
    assert d._get_value() == {"key": "value"}

def test_dict_token_get_child_token():
    d = DictToken({"key": ScalarToken("value", 0, 4, "tokens")}, 0, 4, "tokens")
    t = d._get_child_token("key")
    assert t.value == "value"

def test_dict_token_get_key_token():
    d = DictToken({"key": ScalarToken("value", 0, 4, "tokens")}, 0, 4, "tokens")
    t = d._get_key_token("key")
    assert t.value == "key"

def test_list_token_get_value():
    l = ListToken([ScalarToken("value1", 0, 5, "tokens"), ScalarToken("value2", 6, 11, "tokens")], 0, 11, "tokens")
    assert l._get_value() == ["value1", "value2"]

def test_list_token_get_child_token():
    l = ListToken([ScalarToken("value1", 0, 5, "tokens"), ScalarToken("value2", 6, 11, "tokens")], 0, 11, "tokens")
    t = l._get_child_token(0)
    assert t.value == "value1"