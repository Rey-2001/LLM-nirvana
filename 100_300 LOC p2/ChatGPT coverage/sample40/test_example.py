from api import *
import pytest
from api import PrettyDir

@pytest.fixture
def obj():
    class MyClass:
        def __init__(self):
            self.my_attribute = 42

        def my_method(self):
            return "Hello, World!"

        @property
        def my_property(self):
            return "property value"

    return MyClass()

def test_pretty_dir_repr(obj, capsys):
    pdir = PrettyDir(obj)
    print(pdir)
    captured = capsys.readouterr()
    assert captured.out.strip() == "my_attribute, my_method"

def test_pretty_dir_len(obj):
    pdir = PrettyDir(obj)
    assert len(pdir) == 2

def test_pretty_dir_index(obj):
    pdir = PrettyDir(obj)
    assert pdir.index("my_attribute") == 0
    assert pdir.index("my_method") == 1

def test_pretty_dir_search(obj, capsys):
    pdir = PrettyDir(obj)
    result = pdir.search("attribute")
    assert len(result) == 1
    print(result)
    captured = capsys.readouterr()
    assert captured.out.strip() == "my_attribute"

def test_pretty_dir_properties(obj, capsys):
    pdir = PrettyDir(obj)
    result = pdir.properties
    assert len(result) == 1
    print(result)
    captured = capsys.readouterr()
    assert captured.out.strip() == "my_property: (property)"

def test_pretty_dir_methods(obj, capsys):
    pdir = PrettyDir(obj)
    result = pdir.methods
    assert len(result) == 1
    print(result)
    captured = capsys.readouterr()
    assert captured.out.strip() == "my_method: (function)"

def test_pretty_dir_public(obj, capsys):
    pdir = PrettyDir(obj)
    result = pdir.public
    assert len(result) == 2
    print(result)
    captured = capsys.readouterr()
    assert captured.out.strip() == "my_attribute, my_method"

def test_pretty_dir_own(obj, capsys):
    pdir = PrettyDir(obj)
    result = pdir.own
    assert len(result) == 0
    print(result)
    captured = capsys.readouterr()
    assert captured.out.strip() == ""

def test_pretty_attribute_repr(obj):
    pattr = PrettyAttribute("my_attribute", (), obj.my_attribute)
    assert repr(pattr) == "my_attribute: ()"

def test_pretty_attribute_oneline_doc(obj):
    pattr = PrettyAttribute("my_attribute", (), obj.my_attribute)
    assert pattr.get_oneline_doc() == ""

def test_pretty_attribute_oneline_doc_property(obj):
    pattr = PrettyAttribute("my_property", ("property",), obj.my_property)
    assert (
        pattr.get_oneline_doc() == "@property with getter, property value"
    )

def test_pretty_attribute_oneline_doc_method(obj):
    pattr = PrettyAttribute("my_method", ("function",), obj.my_method)
    assert pattr.get_oneline_doc() == "class method, Hello, World!"

