# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import api as module_0


def test_case_0():
    var_0 = module_0.dataclass_json()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "!T[zZH"
    module_0.dataclass_json(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    var_0 = module_0.dataclass_json(letter_case=bool_0)
    none_type_0 = None
    var_1 = module_0.dataclass_json(undefined=var_0)
    module_0.dataclass_json(bool_0, letter_case=bool_0, undefined=none_type_0)


def test_case_3():
    data_class_json_mixin_0 = module_0.DataClassJsonMixin()
    assert (
        f"{type(module_0.DataClassJsonMixin.from_json).__module__}.{type(module_0.DataClassJsonMixin.from_json).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.DataClassJsonMixin.from_dict).__module__}.{type(module_0.DataClassJsonMixin.from_dict).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.DataClassJsonMixin.schema).__module__}.{type(module_0.DataClassJsonMixin.schema).__qualname__}"
        == "builtins.method"
    )


@pytest.mark.xfail(strict=True)
def test_case_4():
    data_class_json_mixin_0 = module_0.DataClassJsonMixin()
    assert (
        f"{type(module_0.DataClassJsonMixin.from_json).__module__}.{type(module_0.DataClassJsonMixin.from_json).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.DataClassJsonMixin.from_dict).__module__}.{type(module_0.DataClassJsonMixin.from_dict).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.DataClassJsonMixin.schema).__module__}.{type(module_0.DataClassJsonMixin.schema).__qualname__}"
        == "builtins.method"
    )
    none_type_0 = None
    data_class_json_mixin_0.to_json(default=none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    data_class_json_mixin_0 = module_0.DataClassJsonMixin()
    assert (
        f"{type(module_0.DataClassJsonMixin.from_json).__module__}.{type(module_0.DataClassJsonMixin.from_json).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.DataClassJsonMixin.from_dict).__module__}.{type(module_0.DataClassJsonMixin.from_dict).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.DataClassJsonMixin.schema).__module__}.{type(module_0.DataClassJsonMixin.schema).__qualname__}"
        == "builtins.method"
    )
    dict_0 = data_class_json_mixin_0.to_dict()
    none_type_0 = None
    data_class_json_mixin_0.writelines(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    module_0.dataclass_json(bool_0, undefined=bool_0)