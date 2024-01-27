
import pytest
from common import (
    PARAM_KEYWORDS,
    RAISES_KEYWORDS,
    RETURNS_KEYWORDS,
    YIELDS_KEYWORDS,
    DocstringMeta,
    DocstringParam,
    DocstringReturns,
    DocstringRaises,
    DocstringDeprecated,
    Docstring,
)


def test_DocstringMeta():
    args = ["param", "arg"]
    description = "description"
    docstring_meta = DocstringMeta(args, description)
    assert docstring_meta.args == args
    assert docstring_meta.description == description


def test_DocstringParam():
    args = ["param", "arg"]
    description = "description"
    arg_name = "arg_name"
    type_name = "type_name"
    is_optional = True
    default = "default"
    docstring_param = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert docstring_param.args == args
    assert docstring_param.description == description
    assert docstring_param.arg_name == arg_name
    assert docstring_param.type_name == type_name
    assert docstring_param.is_optional == is_optional
    assert docstring_param.default == default


def test_DocstringReturns():
    args = ["return", "returns"]
    description = "description"
    type_name = "type_name"
    is_generator = False
    return_name = "return_name"
    docstring_returns = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert docstring_returns.args == args
    assert docstring_returns.description == description
    assert docstring_returns.type_name == type_name
    assert docstring_returns.is_generator == is_generator
    assert docstring_returns.return_name == return_name


def test_DocstringRaises():
    args = ["raises"]
    description = "description"
    type_name = "type_name"
    docstring_raises = DocstringRaises(args, description, type_name)
    assert docstring_raises.args == args
    assert docstring_raises.description == description
    assert docstring_raises.type_name == type_name


def test_DocstringDeprecated():
    args = ["deprecated"]
    description = "description"
    version = "version"
    docstring_deprecated = DocstringDeprecated(args, description, version)
    assert docstring_deprecated.args == args
    assert docstring_deprecated.description == description
    assert docstring_deprecated.version == version


def test_Docstring():
    docstring = Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []


@pytest.mark.parametrize(
    "args, description, arg_name, type_name, is_optional, default",
    [
        (["param", "arg"], "description", "arg_name", "type_name", True, "default"),
        (["param", "arg"], "description", "arg_name", "type_name", None, "default"),
        (["param", "arg"], "description", "arg_name", None, True, None),
    ],
)
def test_DocstringParam_params_property(args, description, arg_name, type_name, is_optional, default):
    docstring_param = DocstringParam(args, description, arg_name, type_name, is_optional, default)
    assert docstring_param.args == args
    assert docstring_param.description == description
    assert docstring_param.arg_name == arg_name
    assert docstring_param.type_name == type_name
    assert docstring_param.is_optional == is_optional
    assert docstring_param.default == default

    docstring = Docstring()
    docstring.meta.append(docstring_param)
    assert docstring.params == [docstring_param]


@pytest.mark.parametrize(
    "args, description, type_name, return_name",
    [
        (["return", "returns"], "description", "type_name", "return_name"),
        (["return", "returns"], "description", None, "return_name"),
        (["return", "returns"], "description", "type_name", None),
        (["yield", "yields"], "description", "type_name", "return_name"),
    ],
)
def test_DocstringReturns_returns_property(args, description, type_name, return_name):
    is_generator = True if args[0] in YIELDS_KEYWORDS else False
    docstring_returns = DocstringReturns(args, description, type_name, is_generator, return_name)
    assert docstring_returns.args == args
    assert docstring_returns.description == description
    assert docstring_returns.type_name == type_name
    assert docstring_returns.is_generator == is_generator
    assert docstring_returns.return_name == return_name

    docstring = Docstring()
    docstring.meta.append(docstring_returns)
    assert docstring.returns == docstring_returns


@pytest.mark.parametrize(
    "args, description, type_name",
    [
        (["raises"], "description", "type_name"),
        (["raises"], None, "type_name"),
    ]
)
def test_DocstringRaises_raises_property(args, description, type_name):
    docstring_raises = DocstringRaises(args, description, type_name)
    assert docstring_raises.args == args
    assert docstring_raises.description == description
    assert docstring_raises.type_name == type_name

    docstring = Docstring()
    docstring.meta.append(docstring_raises)
    assert docstring.raises == [docstring_raises]


@pytest.mark.parametrize(
    "args, description, version",
    [
        (["deprecated"], "description", "version"),
        (["deprecated"], None, None),
    ]
)
def test_DocstringDeprecated_deprecation_property(args, description, version):
    docstring_deprecated = DocstringDeprecated(args, description, version)
    assert docstring_deprecated.args == args
    assert docstring_deprecated.description == description
    assert docstring_deprecated.version == version

    docstring = Docstring()
    docstring.meta.append(docstring_deprecated)
    assert docstring.deprecation == docstring_deprecated
