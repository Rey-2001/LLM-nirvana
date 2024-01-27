
import pytest
from attr_category import get_attr_category, AttrCategory

def test_get_attr_category():
    # Test for function attribute
    assert get_attr_category('__add__', int.__add__, int) == (AttrCategory.ARITHMETIC, AttrCategory.FUNCTION)

    # Test for class attribute
    assert get_attr_category('__init__', dict.__init__, dict) == (AttrCategory.OBJECT_CUSTOMIZATION, AttrCategory.FUNCTION)

    # Test for module attribute
    assert get_attr_category('__name__', int.__name__, int) == (AttrCategory.MODULE_ATTRIBUTE, AttrCategory.PROPERTY)

    # Test for property attribute
    assert get_attr_category('__class__', int.__class__, int) == (AttrCategory.SPECIAL_ATTRIBUTE, AttrCategory.PROPERTY)

    # Test for descriptor attribute
    assert get_attr_category('__get__', property.__get__, property) == (AttrCategory.DESCRIPTOR, AttrCategory.PROPERTY)

    # Test for static method attribute
    assert get_attr_category('__eq__', dict.__eq__, dict) == (AttrCategory.RICH_COMPARISON, AttrCategory.FUNCTION)
    
    # Test for slotted attribute
    assert get_attr_category('__slots__', tuple.__slots__, tuple) == (AttrCategory.SPECIAL_ATTRIBUTE, AttrCategory.PROPERTY, AttrCategory.SLOT)

    # Test for unknown attribute
    assert get_attr_category('__foobar__', None, None) == (AttrCategory.PROPERTY,)

    # Test for conditional attribute
    assert get_attr_category('__reversed__', iter.__reversed__, iter) == (AttrCategory.ITER, AttrCategory.FUNCTION)
    assert get_attr_category('__reversed__', list.__reversed__, list) == (AttrCategory.CONTAINER, AttrCategory.FUNCTION)
