# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import formats as module_0
import uuid as module_1


def test_case_0():
    time_format_0 = module_0.TimeFormat()
    assert module_0.TimeFormat.errors == {
        "format": "Must be a valid time format.",
        "invalid": "Must be a real time.",
    }


@pytest.mark.xfail(strict=True)
def test_case_1():
    date_format_0 = module_0.DateFormat()
    assert module_0.DateFormat.errors == {
        "format": "Must be a valid date format.",
        "invalid": "Must be a real date.",
    }
    str_0 = "%s(%s)"
    date_format_0.validate(str_0)


def test_case_2():
    base_format_0 = module_0.BaseFormat()
    with pytest.raises(NotImplementedError):
        base_format_0.validate(base_format_0)


def test_case_3():
    u_u_i_d_format_0 = module_0.UUIDFormat()
    assert module_0.UUIDFormat.errors == {"format": "Must be valid UUID format."}
    date_format_0 = module_0.DateFormat()
    assert module_0.DateFormat.errors == {
        "format": "Must be a valid date format.",
        "invalid": "Must be a real date.",
    }
    var_0 = u_u_i_d_format_0.serialize(u_u_i_d_format_0)


def test_case_4():
    u_u_i_d_format_0 = module_0.UUIDFormat()
    assert module_0.UUIDFormat.errors == {"format": "Must be valid UUID format."}
    date_format_0 = module_0.DateFormat()
    assert module_0.DateFormat.errors == {
        "format": "Must be a valid date format.",
        "invalid": "Must be a real date.",
    }
    none_type_0 = None
    var_0 = date_format_0.serialize(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    u_u_i_d_format_0 = module_0.UUIDFormat()
    assert module_0.UUIDFormat.errors == {"format": "Must be valid UUID format."}
    str_0 = u_u_i_d_format_0.serialize(none_type_0)
    assert str_0 == "None"
    u_u_i_d_format_0.validate(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    date_format_0 = module_0.DateFormat()
    assert module_0.DateFormat.errors == {
        "format": "Must be a valid date format.",
        "invalid": "Must be a real date.",
    }
    bool_0 = date_format_0.is_native_type(date_format_0)
    assert bool_0 is False
    date_format_0.serialize(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    u_u_i_d_format_0 = module_0.UUIDFormat()
    assert module_0.UUIDFormat.errors == {"format": "Must be valid UUID format."}
    bool_0 = u_u_i_d_format_0.is_native_type(u_u_i_d_format_0)
    assert bool_0 is False
    str_0 = u_u_i_d_format_0.serialize(bool_0)
    assert str_0 == "False"
    u_u_i_d_format_0.validate(str_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    date_format_0 = module_0.DateFormat()
    assert module_0.DateFormat.errors == {
        "format": "Must be a valid date format.",
        "invalid": "Must be a real date.",
    }
    date_format_0.serialize(date_format_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    time_format_0 = module_0.TimeFormat()
    assert module_0.TimeFormat.errors == {
        "format": "Must be a valid time format.",
        "invalid": "Must be a real time.",
    }
    time_format_0.serialize(time_format_0)


def test_case_10():
    time_format_0 = module_0.TimeFormat()
    assert module_0.TimeFormat.errors == {
        "format": "Must be a valid time format.",
        "invalid": "Must be a real time.",
    }
    none_type_0 = None
    var_0 = time_format_0.serialize(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    date_time_format_0 = module_0.DateTimeFormat()
    assert module_0.DateTimeFormat.errors == {
        "format": "Must be a valid datetime format.",
        "invalid": "Must be a real datetime.",
    }
    date_time_format_0.serialize(date_time_format_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    date_time_format_0 = module_0.DateTimeFormat()
    assert module_0.DateTimeFormat.errors == {
        "format": "Must be a valid datetime format.",
        "invalid": "Must be a real datetime.",
    }
    bool_0 = date_time_format_0.is_native_type(date_time_format_0)
    assert bool_0 is False
    date_time_format_0.serialize(date_time_format_0)


def test_case_13():
    date_time_format_0 = module_0.DateTimeFormat()
    assert module_0.DateTimeFormat.errors == {
        "format": "Must be a valid datetime format.",
        "invalid": "Must be a real datetime.",
    }
    str_0 = ""
    bool_0 = date_time_format_0.is_native_type(date_time_format_0)
    assert bool_0 is False
    bool_1 = date_time_format_0.is_native_type(str_0)
    base_format_0 = module_0.BaseFormat()
    with pytest.raises(NotImplementedError):
        base_format_0.serialize(base_format_0)


@pytest.mark.xfail(strict=True)
def test_case_14():
    time_format_0 = module_0.TimeFormat()
    assert module_0.TimeFormat.errors == {
        "format": "Must be a valid time format.",
        "invalid": "Must be a real time.",
    }
    bool_0 = time_format_0.is_native_type(time_format_0)
    assert bool_0 is False
    time_format_0.serialize(time_format_0)


def test_case_15():
    date_time_format_0 = module_0.DateTimeFormat()
    assert module_0.DateTimeFormat.errors == {
        "format": "Must be a valid datetime format.",
        "invalid": "Must be a real datetime.",
    }
    str_0 = "%s(%s)"
    bool_0 = date_time_format_0.is_native_type(str_0)
    assert bool_0 is False
    none_type_0 = None
    var_0 = date_time_format_0.serialize(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_16():
    date_time_format_0 = module_0.DateTimeFormat()
    assert module_0.DateTimeFormat.errors == {
        "format": "Must be a valid datetime format.",
        "invalid": "Must be a real datetime.",
    }
    str_0 = "%s(%)"
    date_time_format_0.validate(str_0)


def test_case_17():
    base_format_0 = module_0.BaseFormat()
    with pytest.raises(NotImplementedError):
        base_format_0.is_native_type(base_format_0)


@pytest.mark.xfail(strict=True)
def test_case_18():
    str_0 = "]qI&^"
    time_format_0 = module_0.TimeFormat()
    assert module_0.TimeFormat.errors == {
        "format": "Must be a valid time format.",
        "invalid": "Must be a real time.",
    }
    time_format_0.validate(str_0)


def test_case_19():
    u_u_i_d_format_0 = module_0.UUIDFormat()
    assert module_0.UUIDFormat.errors == {"format": "Must be valid UUID format."}
    bool_0 = module_1.uuid4()
    str_0 = u_u_i_d_format_0.serialize(bool_0)
    u_u_i_d_0 = u_u_i_d_format_0.validate(str_0)
    assert f"{type(u_u_i_d_0).__module__}.{type(u_u_i_d_0).__qualname__}" == "uuid.UUID"
