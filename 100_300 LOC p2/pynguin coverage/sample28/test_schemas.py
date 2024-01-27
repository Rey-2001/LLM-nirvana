# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import schemas as module_0
import builtins as module_1
import base as module_2
import fields as module_3


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "}"
    none_type_0 = None
    schema_definitions_0 = module_0.SchemaDefinitions()
    assert (
        f"{type(schema_definitions_0).__module__}.{type(schema_definitions_0).__qualname__}"
        == "schemas.SchemaDefinitions"
    )
    assert len(schema_definitions_0) == 0
    none_type_1 = schema_definitions_0.__setitem__(none_type_0, str_0)
    assert len(schema_definitions_0) == 1
    str_1 = "+w4g"
    dict_0 = {str_1: str_0}
    module_0.Reference(str_0, **dict_0)


def test_case_1():
    schema_definitions_0 = module_0.SchemaDefinitions()
    assert (
        f"{type(schema_definitions_0).__module__}.{type(schema_definitions_0).__qualname__}"
        == "schemas.SchemaDefinitions"
    )
    assert len(schema_definitions_0) == 0
    var_0 = schema_definitions_0.__eq__(schema_definitions_0)
    assert var_0 is True
    none_type_0 = None
    none_type_1 = schema_definitions_0.__setitem__(none_type_0, none_type_0)
    assert len(schema_definitions_0) == 1
    var_1 = schema_definitions_0.items()
    iterator_0 = var_1.__iter__()
    with pytest.raises(AssertionError):
        schema_definitions_0.__setitem__(none_type_1, iterator_0)


def test_case_2():
    bool_0 = False
    none_type_0 = module_0.set_definitions(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.SchemaMetaclass()


def test_case_4():
    schema_0 = module_0.Schema()
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )


def test_case_5():
    schema_0 = module_0.Schema()
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )
    bool_0 = schema_0.__eq__(schema_0)
    assert bool_0 is True


def test_case_6():
    schema_0 = module_0.Schema()
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )
    str_0 = schema_0.__repr__()
    assert str_0 == "Schema()"
    none_type_0 = module_0.set_definitions(schema_0, schema_0)
    var_0 = schema_0.validate(schema_0, strict=schema_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "schemas.Schema"
    assert len(var_0) == 0
    schema_metaclass_0 = schema_0.__eq__(str_0)
    assert schema_metaclass_0 is False


def test_case_7():
    none_type_0 = None
    bytes_0 = b"/\xf6^\nn\x84_k\xfdJ"
    tuple_0 = (bytes_0,)
    schema_0 = module_0.Schema(*tuple_0)
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )
    with pytest.raises(KeyError):
        schema_0.__getitem__(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    schema_0 = module_0.Schema()
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )
    str_0 = schema_0.__repr__()
    assert str_0 == "Schema()"
    bool_0 = schema_0.__eq__(schema_0)
    assert bool_0 is True
    reference_0 = module_0.Reference(str_0)
    assert (
        f"{type(reference_0).__module__}.{type(reference_0).__qualname__}"
        == "schemas.Reference"
    )
    assert reference_0.title == ""
    assert reference_0.description == ""
    assert reference_0.allow_null is False
    assert reference_0.to == "Schema()"
    assert reference_0.definitions is None
    assert module_0.Reference.errors == {"null": "May not be null."}
    assert (
        f"{type(module_0.Reference.target_string).__module__}.{type(module_0.Reference.target_string).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Reference.target).__module__}.{type(module_0.Reference.target).__qualname__}"
        == "builtins.property"
    )
    none_type_0 = module_0.set_definitions(schema_0, schema_0)
    var_0 = schema_0.validate(schema_0, strict=schema_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "schemas.Schema"
    assert len(var_0) == 0
    var_0.__contains__(schema_0)


def test_case_9():
    schema_0 = module_0.Schema()
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )
    str_0 = schema_0.__len__()


@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = "yiBy2E"
    reference_0 = module_0.Reference(str_0)
    assert (
        f"{type(reference_0).__module__}.{type(reference_0).__qualname__}"
        == "schemas.Reference"
    )
    assert reference_0.title == ""
    assert reference_0.description == ""
    assert reference_0.allow_null is False
    assert reference_0.to == "yiBy2E"
    assert reference_0.definitions is None
    assert module_0.Reference.errors == {"null": "May not be null."}
    assert (
        f"{type(module_0.Reference.target_string).__module__}.{type(module_0.Reference.target_string).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Reference.target).__module__}.{type(module_0.Reference.target).__qualname__}"
        == "builtins.property"
    )
    reference_0.validate(str_0, strict=reference_0)


def test_case_11():
    type_0 = module_1.float
    with pytest.raises(AssertionError):
        module_0.Reference(type_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    none_type_0 = None
    str_0 = "$^-"
    reference_0 = module_0.Reference(str_0)
    assert (
        f"{type(reference_0).__module__}.{type(reference_0).__qualname__}"
        == "schemas.Reference"
    )
    assert reference_0.title == ""
    assert reference_0.description == ""
    assert reference_0.allow_null is False
    assert reference_0.to == "$^-"
    assert reference_0.definitions is None
    assert module_0.Reference.errors == {"null": "May not be null."}
    assert (
        f"{type(module_0.Reference.target_string).__module__}.{type(module_0.Reference.target_string).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Reference.target).__module__}.{type(module_0.Reference.target).__qualname__}"
        == "builtins.property"
    )
    var_0 = reference_0.serialize(none_type_0)
    var_0.items()


@pytest.mark.xfail(strict=True)
def test_case_13():
    str_0 = "yiBy2E"
    reference_0 = module_0.Reference(str_0)
    assert (
        f"{type(reference_0).__module__}.{type(reference_0).__qualname__}"
        == "schemas.Reference"
    )
    assert reference_0.title == ""
    assert reference_0.description == ""
    assert reference_0.allow_null is False
    assert reference_0.to == "yiBy2E"
    assert reference_0.definitions is None
    assert module_0.Reference.errors == {"null": "May not be null."}
    assert (
        f"{type(module_0.Reference.target_string).__module__}.{type(module_0.Reference.target_string).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Reference.target).__module__}.{type(module_0.Reference.target).__qualname__}"
        == "builtins.property"
    )
    none_type_0 = None
    validation_result_0 = reference_0.validate_or_error(none_type_0)
    assert (
        f"{type(validation_result_0).__module__}.{type(validation_result_0).__qualname__}"
        == "base.ValidationResult"
    )
    assert validation_result_0.value is None
    assert (
        f"{type(validation_result_0.error).__module__}.{type(validation_result_0.error).__qualname__}"
        == "base.ValidationError"
    )
    assert len(validation_result_0.error) == 1
    reference_0.serialize(reference_0)


def test_case_14():
    schema_definitions_0 = module_0.SchemaDefinitions()
    assert (
        f"{type(schema_definitions_0).__module__}.{type(schema_definitions_0).__qualname__}"
        == "schemas.SchemaDefinitions"
    )
    assert len(schema_definitions_0) == 0


@pytest.mark.xfail(strict=True)
def test_case_15():
    schema_definitions_0 = module_0.SchemaDefinitions()
    assert (
        f"{type(schema_definitions_0).__module__}.{type(schema_definitions_0).__qualname__}"
        == "schemas.SchemaDefinitions"
    )
    assert len(schema_definitions_0) == 0
    schema_definitions_0.__contains__(schema_definitions_0)


@pytest.mark.xfail(strict=True)
def test_case_16():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]
    schema_definitions_0 = module_0.SchemaDefinitions()
    assert (
        f"{type(schema_definitions_0).__module__}.{type(schema_definitions_0).__qualname__}"
        == "schemas.SchemaDefinitions"
    )
    assert len(schema_definitions_0) == 0
    list_1 = [list_0, list_0, schema_definitions_0, list_0]
    module_0.SchemaMetaclass(*list_1)


def test_case_17():
    str_0 = ";]GV\x0bL:HXHR"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    with pytest.raises(TypeError):
        module_0.Schema(**dict_0)


def test_case_18():
    str_0 = "yiBy2E"
    reference_0 = module_0.Reference(str_0)
    assert (
        f"{type(reference_0).__module__}.{type(reference_0).__qualname__}"
        == "schemas.Reference"
    )
    assert reference_0.title == ""
    assert reference_0.description == ""
    assert reference_0.allow_null is False
    assert reference_0.to == "yiBy2E"
    assert reference_0.definitions is None
    assert module_0.Reference.errors == {"null": "May not be null."}
    assert (
        f"{type(module_0.Reference.target_string).__module__}.{type(module_0.Reference.target_string).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Reference.target).__module__}.{type(module_0.Reference.target).__qualname__}"
        == "builtins.property"
    )
    none_type_0 = None
    validation_result_0 = reference_0.validate_or_error(none_type_0)
    assert (
        f"{type(validation_result_0).__module__}.{type(validation_result_0).__qualname__}"
        == "base.ValidationResult"
    )
    assert validation_result_0.value is None
    assert (
        f"{type(validation_result_0.error).__module__}.{type(validation_result_0.error).__qualname__}"
        == "base.ValidationError"
    )
    assert len(validation_result_0.error) == 1


def test_case_19():
    schema_0 = module_0.Schema()
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )
    var_0 = schema_0.validate(schema_0, strict=schema_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "schemas.Schema"
    assert len(var_0) == 0


def test_case_20():
    schema_0 = module_0.Schema()
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )
    str_0 = schema_0.__repr__()
    assert str_0 == "Schema()"


@pytest.mark.xfail(strict=True)
def test_case_21():
    str_0 = "UoRIV>9U~}jNJ/\n>"
    list_0 = []
    dict_0 = {str_0: str_0, str_0: list_0}
    schema_definitions_0 = module_0.SchemaDefinitions(*list_0, **dict_0)
    assert (
        f"{type(schema_definitions_0).__module__}.{type(schema_definitions_0).__qualname__}"
        == "schemas.SchemaDefinitions"
    )
    assert len(schema_definitions_0) == 1
    var_0 = schema_definitions_0.__delitem__(str_0)
    assert len(schema_definitions_0) == 0
    var_0.__contains__(str_0)


def test_case_22():
    bytes_0 = b"/\xf6^\nn\x84_k\xfdJ"
    tuple_0 = (bytes_0,)
    schema_0 = module_0.Schema(*tuple_0)
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )


def test_case_23():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0]
    with pytest.raises(AssertionError):
        module_0.Schema(*list_0, **dict_0)


def test_case_24():
    schema_0 = module_0.Schema()
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )
    str_0 = schema_0.__str__()
    assert str_0 == "Schema()"
    bool_0 = schema_0.__eq__(schema_0)
    assert bool_0 is True
    none_type_0 = module_0.set_definitions(schema_0, schema_0)
    var_0 = schema_0.validate(schema_0, strict=schema_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "schemas.Schema"
    assert len(var_0) == 0
    with pytest.raises(module_2.ValidationError):
        var_0.validate(none_type_0, strict=bool_0)


@pytest.mark.xfail(strict=True)
def test_case_25():
    schema_0 = module_0.Schema()
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )
    str_0 = schema_0.__repr__()
    assert str_0 == "Schema()"
    bool_0 = schema_0.__eq__(schema_0)
    assert bool_0 is True
    reference_0 = module_0.Reference(str_0)
    assert (
        f"{type(reference_0).__module__}.{type(reference_0).__qualname__}"
        == "schemas.Reference"
    )
    assert reference_0.title == ""
    assert reference_0.description == ""
    assert reference_0.allow_null is False
    assert reference_0.to == "Schema()"
    assert reference_0.definitions is None
    assert module_0.Reference.errors == {"null": "May not be null."}
    assert (
        f"{type(module_0.Reference.target_string).__module__}.{type(module_0.Reference.target_string).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Reference.target).__module__}.{type(module_0.Reference.target).__qualname__}"
        == "builtins.property"
    )
    var_0 = schema_0.__eq__(str_0)
    assert var_0 is False
    none_type_0 = module_0.set_definitions(reference_0, var_0)
    assert reference_0.definitions is False
    reference_0.validate(var_0)


@pytest.mark.xfail(strict=True)
def test_case_26():
    schema_0 = module_0.Schema()
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )
    str_0 = schema_0.__repr__()
    assert str_0 == "Schema()"
    none_type_0 = None
    var_0 = schema_0.keys()
    reference_0 = module_0.Reference(str_0, none_type_0)
    assert (
        f"{type(reference_0).__module__}.{type(reference_0).__qualname__}"
        == "schemas.Reference"
    )
    assert reference_0.title == ""
    assert reference_0.description == ""
    assert reference_0.allow_null is False
    assert reference_0.to == "Schema()"
    assert reference_0.definitions is None
    assert module_0.Reference.errors == {"null": "May not be null."}
    assert (
        f"{type(module_0.Reference.target_string).__module__}.{type(module_0.Reference.target_string).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Reference.target).__module__}.{type(module_0.Reference.target).__qualname__}"
        == "builtins.property"
    )
    var_1 = schema_0.keys()
    none_type_1 = module_0.set_definitions(reference_0, var_1)
    assert (
        f"{type(reference_0.definitions).__module__}.{type(reference_0.definitions).__qualname__}"
        == "collections.abc.KeysView"
    )
    assert len(reference_0.definitions) == 0
    var_2 = schema_0.__eq__(none_type_1)
    assert var_2 is False
    none_type_2 = module_0.set_definitions(reference_0, var_2)
    reference_0.validate(str_0, strict=none_type_0)


def test_case_27():
    str_0 = ";KIyw"
    none_type_0 = None
    list_0 = [none_type_0]
    str_1 = "Hk?-"
    dict_0 = {str_1: str_0, str_0: str_1}
    with pytest.raises(AssertionError):
        module_0.Schema(*list_0, **dict_0)


def test_case_28():
    schema_0 = module_0.Schema()
    assert (
        f"{type(schema_0).__module__}.{type(schema_0).__qualname__}" == "schemas.Schema"
    )
    assert len(schema_0) == 0
    assert (
        f"{type(module_0.Schema.make_validator).__module__}.{type(module_0.Schema.make_validator).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate).__module__}.{type(module_0.Schema.validate).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.validate_or_error).__module__}.{type(module_0.Schema.validate_or_error).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.Schema.is_sparse).__module__}.{type(module_0.Schema.is_sparse).__qualname__}"
        == "builtins.property"
    )
    var_0 = schema_0.values()
    validation_result_0 = schema_0.validate_or_error(var_0)
    assert (
        f"{type(validation_result_0).__module__}.{type(validation_result_0).__qualname__}"
        == "base.ValidationResult"
    )
    assert validation_result_0.value is None
    assert (
        f"{type(validation_result_0.error).__module__}.{type(validation_result_0.error).__qualname__}"
        == "base.ValidationError"
    )
    assert len(validation_result_0.error) == 1


def test_case_29():
    none_type_0 = None
    object_0 = module_3.Object(
        properties=none_type_0,
        property_names=none_type_0,
        max_properties=none_type_0,
        required=none_type_0,
    )
    none_type_1 = module_0.set_definitions(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_30():
    type_0 = module_0.Schema
    dict_0 = {}
    reference_0 = module_0.Reference(type_0, **dict_0)
    assert (
        f"{type(reference_0).__module__}.{type(reference_0).__qualname__}"
        == "schemas.Reference"
    )
    assert reference_0.title == ""
    assert reference_0.description == ""
    assert reference_0.allow_null is False
    assert reference_0.definitions is None
    assert module_0.Reference.errors == {"null": "May not be null."}
    assert (
        f"{type(module_0.Reference.target_string).__module__}.{type(module_0.Reference.target_string).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Reference.target).__module__}.{type(module_0.Reference.target).__qualname__}"
        == "builtins.property"
    )
    str_0 = "J"
    list_0 = [str_0, str_0, dict_0, dict_0]
    module_0.SchemaMetaclass(*list_0, **dict_0)


def test_case_31():
    array_0 = module_3.Array()
    none_type_0 = module_0.set_definitions(array_0, array_0)


@pytest.mark.xfail(strict=True)
def test_case_32():
    type_0 = module_0.Schema
    dict_0 = {}
    reference_0 = module_0.Reference(type_0, **dict_0)
    assert (
        f"{type(reference_0).__module__}.{type(reference_0).__qualname__}"
        == "schemas.Reference"
    )
    assert reference_0.title == ""
    assert reference_0.description == ""
    assert reference_0.allow_null is False
    assert reference_0.definitions is None
    assert module_0.Reference.errors == {"null": "May not be null."}
    assert (
        f"{type(module_0.Reference.target_string).__module__}.{type(module_0.Reference.target_string).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Reference.target).__module__}.{type(module_0.Reference.target).__qualname__}"
        == "builtins.property"
    )
    reference_0.validate(type_0)