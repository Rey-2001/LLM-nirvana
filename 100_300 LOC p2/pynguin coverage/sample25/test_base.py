# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import base as module_0


def test_case_0():
    str_0 = "cfI`g:CV\x0c>\tI"
    parse_error_0 = module_0.ParseError(text=str_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1


def test_case_1():
    tuple_0 = ()
    base_error_0 = module_0.BaseError(text=tuple_0, code=tuple_0, key=tuple_0)
    assert (
        f"{type(base_error_0).__module__}.{type(base_error_0).__qualname__}"
        == "base.BaseError"
    )
    assert len(base_error_0) == 1


def test_case_2():
    str_0 = "_\x0c18*[M;z*{nUJ!pwW"
    with pytest.raises(AssertionError):
        module_0.BaseError(key=str_0)


def test_case_3():
    list_0 = []
    with pytest.raises(AssertionError):
        module_0.BaseError(messages=list_0)


def test_case_4():
    str_0 = ""
    validation_error_0 = module_0.ValidationError(text=str_0, key=str_0)
    assert (
        f"{type(validation_error_0).__module__}.{type(validation_error_0).__qualname__}"
        == "base.ValidationError"
    )
    assert len(validation_error_0) == 1
    int_0 = validation_error_0.__len__()
    assert int_0 == 1
    bool_0 = validation_error_0.__eq__(int_0)
    assert bool_0 is False


def test_case_5():
    str_0 = "cfI`g:CV\x0c>\tI"
    parse_error_0 = module_0.ParseError(text=str_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    str_1 = parse_error_0.__repr__()
    assert str_1 == "ParseError(text='cfI`g:CV\\x0c>\\tI', code='custom')"


def test_case_6():
    validation_result_0 = module_0.ValidationResult()


@pytest.mark.xfail(strict=True)
def test_case_7():
    none_type_0 = None
    position_0 = module_0.Position(none_type_0, none_type_0, none_type_0)
    none_type_1 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, key=str_0, position=str_0, start_position=none_type_1
    )
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position == "cfPI`g:CXV\x0cS\tI"
    int_0 = message_0.__hash__()
    assert int_0 == 5322473327714082801
    bool_0 = message_0.__eq__(message_0)
    assert bool_0 is True
    parse_error_0 = module_0.ParseError(text=str_0, position=none_type_1)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    validation_result_0 = module_0.ValidationResult(value=message_0)
    assert (
        f"{type(validation_result_0).__module__}.{type(validation_result_0).__qualname__}"
        == "base.ValidationResult"
    )
    assert (
        f"{type(validation_result_0.value).__module__}.{type(validation_result_0.value).__qualname__}"
        == "base.Message"
    )
    assert validation_result_0.error is None
    var_0 = parse_error_0.__eq__(str_0)
    assert var_0 is False
    int_1 = var_0.__hash__()
    assert int_1 == 0
    list_0 = parse_error_0.messages()
    str_1 = message_0.__repr__()
    assert (
        str_1
        == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom', index=['cfPI`g:CXV\\x0cS\\tI'], position='cfPI`g:CXV\\x0cS\\tI')"
    )
    bool_1 = parse_error_0.__eq__(list_0)
    assert bool_1 is False
    str_2 = parse_error_0.__repr__()
    assert str_2 == "ParseError(text='cfPI`g:CXV\\x0cS\\tI', code='custom')"
    str_3 = parse_error_0.__str__()
    assert str_3 == "cfPI`g:CXV\x0cS\tI"
    str_4 = var_0.__repr__()
    assert str_4 == "False"
    bool_2 = position_0.__eq__(position_0)
    assert bool_2 is True
    bool_3 = True
    bool_4 = position_0.__eq__(bool_3)
    assert bool_4 is False
    module_0.BaseError(key=none_type_1, messages=message_0)


def test_case_8():
    bool_0 = False
    position_0 = module_0.Position(bool_0, bool_0, bool_0)


def test_case_9():
    none_type_0 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, key=str_0, position=str_0, start_position=none_type_0
    )
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position == "cfPI`g:CXV\x0cS\tI"
    int_0 = message_0.__hash__()
    assert int_0 == 5322473327714082801


def test_case_10():
    dict_0 = {}
    str_0 = ".b}*;f=GbU\n}bY2#"
    parse_error_0 = module_0.ParseError(text=dict_0, code=str_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    iterator_0 = parse_error_0.__iter__()


def test_case_11():
    bool_0 = False
    none_type_0 = None
    parse_error_0 = module_0.ParseError(text=bool_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    bool_1 = parse_error_0.__eq__(bool_0)
    assert bool_1 is False
    var_0 = parse_error_0.values()
    assert len(var_0) == 1
    iterator_0 = parse_error_0.get(none_type_0)
    with pytest.raises(AssertionError):
        module_0.BaseError(text=iterator_0, code=iterator_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    none_type_0 = None
    str_0 = "cfPI`g:CXV\x0cSsy\tI"
    message_0 = module_0.Message(
        text=str_0, key=str_0, position=str_0, start_position=none_type_0
    )
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cSsy\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cSsy\tI"
    assert message_0.end_position == "cfPI`g:CXV\x0cSsy\tI"
    module_0.ParseError(key=none_type_0, messages=none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
    dict_0 = {}
    str_0 = "mqf?;"
    module_0.ParseError(text=dict_0, code=str_0, messages=dict_0)


def test_case_14():
    str_0 = "\nu8RT$,0pK"
    message_0 = module_0.Message(text=str_0, start_position=str_0)
    assert (
        f"{type(message_0).__module__}.{type(message_0).__qualname__}" == "base.Message"
    )
    assert message_0.text == "\nu8RT$,0pK"
    assert message_0.code == "custom"
    assert message_0.index == []
    assert message_0.start_position == "\nu8RT$,0pK"
    assert message_0.end_position is None
    str_1 = "Y#{j7Z&qK+<XAEdw"
    with pytest.raises(AssertionError):
        module_0.ValidationResult(value=str_1, error=str_1)


def test_case_15():
    none_type_0 = None
    position_0 = module_0.Position(none_type_0, none_type_0, none_type_0)
    none_type_1 = None
    validation_result_0 = module_0.ValidationResult(value=none_type_1)
    bool_0 = position_0.__eq__(position_0)
    assert bool_0 is True
    bool_1 = True
    bool_2 = position_0.__eq__(bool_1)
    assert bool_2 is False


def test_case_16():
    none_type_0 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, key=str_0, position=str_0, start_position=none_type_0
    )
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position == "cfPI`g:CXV\x0cS\tI"
    int_0 = message_0.__hash__()
    assert int_0 == 5322473327714082801
    str_1 = message_0.__repr__()
    assert (
        str_1
        == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom', index=['cfPI`g:CXV\\x0cS\\tI'], position='cfPI`g:CXV\\x0cS\\tI')"
    )


@pytest.mark.xfail(strict=True)
def test_case_17():
    bool_0 = False
    none_type_0 = None
    base_error_0 = module_0.BaseError(
        text=bool_0, position=none_type_0, messages=none_type_0
    )
    assert (
        f"{type(base_error_0).__module__}.{type(base_error_0).__qualname__}"
        == "base.BaseError"
    )
    assert len(base_error_0) == 1
    base_error_0.__getitem__(base_error_0)


def test_case_18():
    bytes_0 = b"\xec\xa18.\xbc\x83\xa3\xed<\x96bH&\x94\xb1\x93!"
    none_type_0 = None
    with pytest.raises(AssertionError):
        module_0.BaseError(code=bytes_0, position=none_type_0, messages=bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_19():
    none_type_0 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, key=str_0, position=str_0, start_position=none_type_0
    )
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position == "cfPI`g:CXV\x0cS\tI"
    bool_0 = message_0.__eq__(none_type_0)
    assert bool_0 is False
    parse_error_0 = module_0.ParseError(text=str_0, position=none_type_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    validation_result_0 = module_0.ValidationResult(value=none_type_0)
    var_0 = parse_error_0.__eq__(str_0)
    assert var_0 is False
    int_0 = 1
    list_0 = parse_error_0.messages()
    var_1 = parse_error_0.__eq__(int_0)
    assert var_1 is False
    str_1 = message_0.__repr__()
    assert (
        str_1
        == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom', index=['cfPI`g:CXV\\x0cS\\tI'], position='cfPI`g:CXV\\x0cS\\tI')"
    )
    bool_1 = var_1.__eq__(list_0)
    str_2 = parse_error_0.__repr__()
    assert str_2 == "ParseError(text='cfPI`g:CXV\\x0cS\\tI', code='custom')"
    str_3 = parse_error_0.__str__()
    assert str_3 == "cfPI`g:CXV\x0cS\tI"
    str_4 = var_0.__repr__()
    assert str_4 == "False"
    module_0.BaseError(key=none_type_0, messages=message_0)


def test_case_20():
    str_0 = ""
    validation_error_0 = module_0.ValidationError(text=str_0, key=str_0)
    assert (
        f"{type(validation_error_0).__module__}.{type(validation_error_0).__qualname__}"
        == "base.ValidationError"
    )
    assert len(validation_error_0) == 1
    int_0 = validation_error_0.__len__()
    assert int_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_21():
    validation_result_0 = module_0.ValidationResult()
    bool_0 = validation_result_0.__bool__()
    dict_0 = {}
    dict_0.messages()


def test_case_22():
    str_0 = ""
    str_1 = "cfPI`g:CXV\x0cSsy\tI"
    list_0 = [str_1, str_0]
    none_type_0 = None
    with pytest.raises(AssertionError):
        module_0.Message(
            text=str_0,
            key=str_0,
            index=list_0,
            position=none_type_0,
            start_position=none_type_0,
            end_position=str_1,
        )


def test_case_23():
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(text=str_0, key=str_0, start_position=str_0)
    assert (
        f"{type(message_0).__module__}.{type(message_0).__qualname__}" == "base.Message"
    )
    assert message_0.text == "cfPI`g:CXV\x0cS\tI"
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position is None
    parse_error_0 = module_0.ParseError(text=str_0, position=message_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    bool_0 = parse_error_0.__eq__(parse_error_0)
    assert bool_0 is False
    var_0 = parse_error_0.__iter__()
    var_1 = parse_error_0.values()
    assert len(var_1) == 1
    str_1 = var_0.__repr__()
    str_2 = parse_error_0.__str__()
    assert str_2 == "cfPI`g:CXV\x0cS\tI"
    with pytest.raises(AssertionError):
        module_0.BaseError(key=var_0, messages=var_1)


def test_case_24():
    none_type_0 = None
    validation_result_0 = module_0.ValidationResult()
    position_0 = module_0.Position(none_type_0, none_type_0, none_type_0)
    none_type_1 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, key=str_0, position=str_0, start_position=none_type_1
    )
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position == "cfPI`g:CXV\x0cS\tI"
    int_0 = message_0.__hash__()
    assert int_0 == 5322473327714082801
    bool_0 = message_0.__eq__(message_0)
    assert bool_0 is True
    parse_error_0 = module_0.ParseError(text=int_0, key=str_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    int_1 = 1
    list_0 = parse_error_0.messages(add_prefix=int_1)
    str_1 = parse_error_0.values()
    assert len(str_1) == 1
    bool_1 = position_0.__eq__(list_0)
    assert bool_1 is False
    str_2 = parse_error_0.__repr__()
    assert (
        str_2
        == "ParseError([Message(text=5322473327714082801, code='custom', index=['cfPI`g:CXV\\x0cS\\tI'])])"
    )
    str_3 = parse_error_0.__str__()
    assert str_3 == "{'cfPI`g:CXV\\x0cS\\tI': 5322473327714082801}"
    str_4 = position_0.__repr__()
    assert str_4 == "Position(line_no=None, column_no=None, char_index=None)"
    bool_2 = position_0.__eq__(message_0)
    bool_3 = position_0.__eq__(validation_result_0)
    base_error_0 = module_0.BaseError(messages=list_0)
    assert len(base_error_0) == 1


def test_case_25():
    validation_result_0 = module_0.ValidationResult()
    str_0 = validation_result_0.__repr__()
    assert str_0 == "ValidationResult(value=None)"


def test_case_26():
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(text=str_0, key=str_0, start_position=str_0)
    assert (
        f"{type(message_0).__module__}.{type(message_0).__qualname__}" == "base.Message"
    )
    assert message_0.text == "cfPI`g:CXV\x0cS\tI"
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position is None
    parse_error_0 = module_0.ParseError(text=str_0, position=message_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    bool_0 = parse_error_0.__eq__(parse_error_0)
    assert bool_0 is False
    var_0 = parse_error_0.__iter__()
    str_1 = var_0.__repr__()
    str_2 = parse_error_0.__str__()
    assert str_2 == "cfPI`g:CXV\x0cS\tI"


@pytest.mark.xfail(strict=True)
def test_case_27():
    none_type_0 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=none_type_0, position=none_type_0, start_position=str_0
    )
    assert (
        f"{type(message_0).__module__}.{type(message_0).__qualname__}" == "base.Message"
    )
    assert message_0.text is None
    assert message_0.code == "custom"
    assert message_0.index == []
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position is None
    str_1 = message_0.__repr__()
    assert (
        str_1
        == "Message(text=None, code='custom', start_position='cfPI`g:CXV\\x0cS\\tI', end_position=None)"
    )
    bool_0 = message_0.__eq__(str_1)
    assert bool_0 is False
    message_1 = module_0.Message(
        text=str_1, position=none_type_0, end_position=none_type_0
    )
    assert (
        message_1.text
        == "Message(text=None, code='custom', start_position='cfPI`g:CXV\\x0cS\\tI', end_position=None)"
    )
    assert message_1.code == "custom"
    assert message_1.index == []
    module_0.ParseError()


@pytest.mark.xfail(strict=True)
def test_case_28():
    none_type_0 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, key=str_0, position=str_0, start_position=none_type_0
    )
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position == "cfPI`g:CXV\x0cS\tI"
    bool_0 = message_0.__eq__(message_0)
    assert bool_0 is True
    bool_1 = str_0.__eq__(str_0)
    module_0.ValidationError(key=bool_0)


def test_case_29():
    none_type_0 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    bytes_0 = b"+\xd0"
    message_0 = module_0.Message(text=str_0, key=str_0, position=bytes_0)
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == b"+\xd0"
    assert message_0.end_position == b"+\xd0"
    bool_0 = message_0.__eq__(bytes_0)
    assert bool_0 is False
    parse_error_0 = module_0.ParseError(
        text=str_0, key=none_type_0, messages=none_type_0
    )
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    validation_result_0 = module_0.ValidationResult(error=message_0)
    assert (
        f"{type(validation_result_0).__module__}.{type(validation_result_0).__qualname__}"
        == "base.ValidationResult"
    )
    assert validation_result_0.value is None
    assert (
        f"{type(validation_result_0.error).__module__}.{type(validation_result_0.error).__qualname__}"
        == "base.Message"
    )
    str_1 = message_0.__repr__()
    assert (
        str_1
        == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom', index=['cfPI`g:CXV\\x0cS\\tI'], position=b'+\\xd0')"
    )
    str_2 = validation_result_0.__repr__()
    assert (
        str_2
        == "ValidationResult(error=Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom', index=['cfPI`g:CXV\\x0cS\\tI'], position=b'+\\xd0'))"
    )
    with pytest.raises(AssertionError):
        module_0.BaseError()


def test_case_30():
    bool_0 = False
    position_0 = module_0.Position(bool_0, bool_0, bool_0)
    str_0 = position_0.__repr__()
    assert str_0 == "Position(line_no=False, column_no=False, char_index=False)"


def test_case_31():
    str_0 = "cfPI`g:CXV\x0cS\tI"
    with pytest.raises(AssertionError):
        module_0.Message(text=str_0, key=str_0, position=str_0, start_position=str_0)


def test_case_32():
    none_type_0 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, key=str_0, position=str_0, start_position=none_type_0
    )
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position == "cfPI`g:CXV\x0cS\tI"
    bool_0 = message_0.__eq__(message_0)
    assert bool_0 is True
    parse_error_0 = module_0.ParseError(text=str_0, position=none_type_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    validation_result_0 = module_0.ValidationResult(value=none_type_0)
    var_0 = parse_error_0.__eq__(str_0)
    assert var_0 is False
    int_0 = 1
    list_0 = parse_error_0.messages()
    var_1 = parse_error_0.__eq__(int_0)
    assert var_1 is False
    str_1 = message_0.__repr__()
    assert (
        str_1
        == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom', index=['cfPI`g:CXV\\x0cS\\tI'], position='cfPI`g:CXV\\x0cS\\tI')"
    )
    with pytest.raises(AssertionError):
        module_0.Message(
            text=none_type_0,
            code=str_1,
            key=str_1,
            index=none_type_0,
            position=var_0,
            end_position=str_1,
        )


@pytest.mark.xfail(strict=True)
def test_case_33():
    none_type_0 = None
    bool_0 = False
    dict_0 = {bool_0: none_type_0}
    tuple_0 = (dict_0,)
    module_0.ValidationError(text=none_type_0, position=bool_0, messages=tuple_0)


def test_case_34():
    none_type_0 = None
    position_0 = module_0.Position(none_type_0, none_type_0, none_type_0)
    bool_0 = position_0.__eq__(position_0)
    assert bool_0 is True


@pytest.mark.xfail(strict=True)
def test_case_35():
    none_type_0 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, key=str_0, position=str_0, start_position=none_type_0
    )
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position == "cfPI`g:CXV\x0cS\tI"
    bool_0 = message_0.__eq__(message_0)
    assert bool_0 is True
    str_1 = "lR&,q_DOtLB%n 5M"
    message_1 = module_0.Message(text=str_1)
    assert message_1.code == "custom"
    assert message_1.index == []
    str_2 = message_0.__repr__()
    assert (
        str_2
        == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom', index=['cfPI`g:CXV\\x0cS\\tI'], position='cfPI`g:CXV\\x0cS\\tI')"
    )
    bool_1 = message_0.__eq__(message_1)
    assert bool_1 is False
    message_2 = module_0.Message(text=str_0, end_position=bool_1)
    assert (
        f"{type(message_2).__module__}.{type(message_2).__qualname__}" == "base.Message"
    )
    assert message_2.text == "cfPI`g:CXV\x0cS\tI"
    assert message_2.code == "custom"
    assert message_2.index == []
    assert message_2.start_position is None
    assert message_2.end_position is False
    module_0.ParseError(code=str_2, key=str_2, position=message_0)


def test_case_36():
    none_type_0 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, key=str_0, position=str_0, start_position=none_type_0
    )
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position == "cfPI`g:CXV\x0cS\tI"
    str_1 = message_0.__repr__()
    assert (
        str_1
        == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom', index=['cfPI`g:CXV\\x0cS\\tI'], position='cfPI`g:CXV\\x0cS\\tI')"
    )
    bool_0 = message_0.__eq__(message_0)
    assert bool_0 is True
    message_1 = module_0.Message(
        text=none_type_0, key=none_type_0, start_position=none_type_0
    )
    assert message_1.code == "custom"
    assert message_1.index == []
    parse_error_0 = module_0.ParseError(text=str_0, position=none_type_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    int_0 = message_1.__hash__()
    assert int_0 == -3236363584314578347
    bool_1 = parse_error_0.__eq__(parse_error_0)
    assert bool_1 is False
    bool_2 = message_0.__eq__(none_type_0)
    assert bool_2 is False
    validation_result_0 = module_0.ValidationResult(value=none_type_0)
    var_0 = parse_error_0.__iter__()
    int_1 = 1
    bool_3 = True
    position_0 = module_0.Position(bool_3, int_1, var_0)
    assert (
        f"{type(position_0.char_index).__module__}.{type(position_0.char_index).__qualname__}"
        == "builtins.dict_keyiterator"
    )
    str_2 = message_1.__repr__()
    assert str_2 == "Message(text=None, code='custom')"
    bool_4 = False
    position_1 = module_0.Position(message_0, bool_4, int_1)
    bool_5 = position_1.__eq__(position_0)
    assert bool_5 is False
    str_3 = parse_error_0.__str__()
    assert str_3 == "cfPI`g:CXV\x0cS\tI"
    str_4 = validation_result_0.__repr__()
    assert str_4 == "ValidationResult(value=None)"
    with pytest.raises(AssertionError):
        module_0.BaseError(code=str_1)


@pytest.mark.xfail(strict=True)
def test_case_37():
    none_type_0 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, key=str_0, position=str_0, start_position=none_type_0
    )
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position == "cfPI`g:CXV\x0cS\tI"
    str_1 = message_0.__repr__()
    assert (
        str_1
        == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom', index=['cfPI`g:CXV\\x0cS\\tI'], position='cfPI`g:CXV\\x0cS\\tI')"
    )
    message_1 = module_0.Message(text=str_0, end_position=none_type_0)
    assert message_1.code == "custom"
    assert message_1.index == []
    bool_0 = message_1.__eq__(message_0)
    assert bool_0 is False
    str_2 = '0b"ch=*m,\\'
    message_2 = module_0.Message(
        text=str_2, code=str_2, index=message_0, position=none_type_0
    )
    assert (
        f"{type(message_2).__module__}.{type(message_2).__qualname__}" == "base.Message"
    )
    assert message_2.text == '0b"ch=*m,\\'
    assert message_2.code == '0b"ch=*m,\\'
    assert (
        f"{type(message_2.index).__module__}.{type(message_2.index).__qualname__}"
        == "base.Message"
    )
    assert message_2.start_position is None
    assert message_2.end_position is None
    parse_error_0 = module_0.ParseError(text=bool_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    var_0 = parse_error_0.keys()
    assert len(var_0) == 1
    bool_1 = parse_error_0.__eq__(var_0)
    assert bool_1 is False
    validation_result_0 = module_0.ValidationResult(value=str_1)
    assert (
        f"{type(validation_result_0).__module__}.{type(validation_result_0).__qualname__}"
        == "base.ValidationResult"
    )
    assert (
        validation_result_0.value
        == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom', index=['cfPI`g:CXV\\x0cS\\tI'], position='cfPI`g:CXV\\x0cS\\tI')"
    )
    assert validation_result_0.error is None
    module_0.ParseError(position=var_0)


def test_case_38():
    none_type_0 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, key=none_type_0, index=none_type_0, start_position=none_type_0
    )
    assert message_0.code == "custom"
    assert message_0.index == []
    str_1 = message_0.__repr__()
    assert str_1 == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom')"
    bool_0 = message_0.__eq__(none_type_0)
    assert bool_0 is False
    message_1 = module_0.Message(text=str_0, code=str_1, key=none_type_0)
    assert message_1.code == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom')"
    assert message_1.index == []
    parse_error_0 = module_0.ParseError(text=str_1)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    int_0 = message_0.__hash__()
    assert int_0 == -3236363584314578347
    bool_1 = parse_error_0.__eq__(message_0)
    assert bool_1 is False
    bool_2 = message_1.__eq__(message_0)
    assert bool_2 is False
    validation_result_0 = module_0.ValidationResult()
    var_0 = parse_error_0.__iter__()
    var_1 = parse_error_0.values()
    assert len(var_1) == 1
    bool_3 = True
    bool_4 = False
    position_0 = module_0.Position(var_0, bool_3, bool_4)
    assert (
        f"{type(position_0.line_no).__module__}.{type(position_0.line_no).__qualname__}"
        == "builtins.dict_keyiterator"
    )
    str_2 = var_1.__repr__()
    assert (
        str_2
        == "ValuesView(ParseError(text=\"Message(text='cfPI`g:CXV\\\\x0cS\\\\tI', code='custom')\", code='custom'))"
    )
    bool_5 = var_1.__eq__(str_2)
    str_3 = var_1.__str__()
    assert (
        str_3
        == "ValuesView(ParseError(text=\"Message(text='cfPI`g:CXV\\\\x0cS\\\\tI', code='custom')\", code='custom'))"
    )
    str_4 = var_0.__repr__()
    with pytest.raises(AssertionError):
        module_0.BaseError()


@pytest.mark.xfail(strict=True)
def test_case_39():
    str_0 = "cfPI`g:CXV\x0cS\tI"
    validation_result_0 = module_0.ValidationResult(value=str_0)
    assert (
        f"{type(validation_result_0).__module__}.{type(validation_result_0).__qualname__}"
        == "base.ValidationResult"
    )
    assert validation_result_0.value == "cfPI`g:CXV\x0cS\tI"
    assert validation_result_0.error is None
    int_0 = -3814
    position_0 = module_0.Position(str_0, int_0, str_0)
    none_type_0 = None
    validation_error_0 = module_0.ValidationError(text=validation_result_0, key=str_0)
    assert (
        f"{type(validation_error_0).__module__}.{type(validation_error_0).__qualname__}"
        == "base.ValidationError"
    )
    assert len(validation_error_0) == 1
    message_0 = module_0.Message(
        text=validation_error_0,
        code=validation_error_0,
        key=validation_result_0,
        position=position_0,
        start_position=none_type_0,
    )
    assert len(message_0.text) == 1
    assert len(message_0.code) == 1
    assert len(message_0.index) == 1
    assert (
        f"{type(message_0.start_position).__module__}.{type(message_0.start_position).__qualname__}"
        == "base.Position"
    )
    assert (
        f"{type(message_0.end_position).__module__}.{type(message_0.end_position).__qualname__}"
        == "base.Position"
    )
    int_1 = message_0.__hash__()
    bool_0 = message_0.__eq__(message_0)
    assert bool_0 is True
    module_0.ParseError(key=validation_error_0, position=position_0)


@pytest.mark.xfail(strict=True)
def test_case_40():
    none_type_0 = None
    bytes_0 = b"\xc4z9\x9d7`y\xb2\x93\x0e\xda\xa8Y"
    validation_result_0 = module_0.ValidationResult(error=bytes_0)
    assert (
        f"{type(validation_result_0).__module__}.{type(validation_result_0).__qualname__}"
        == "base.ValidationResult"
    )
    assert validation_result_0.value is None
    assert validation_result_0.error == b"\xc4z9\x9d7`y\xb2\x93\x0e\xda\xa8Y"
    position_0 = module_0.Position(none_type_0, bytes_0, none_type_0)
    none_type_1 = None
    bool_0 = validation_result_0.__bool__()
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, code=none_type_1, index=validation_result_0, position=position_0
    )
    assert (
        f"{type(message_0).__module__}.{type(message_0).__qualname__}" == "base.Message"
    )
    assert message_0.text == "cfPI`g:CXV\x0cS\tI"
    assert message_0.code == "custom"
    assert (
        f"{type(message_0.index).__module__}.{type(message_0.index).__qualname__}"
        == "base.ValidationResult"
    )
    assert (
        f"{type(message_0.start_position).__module__}.{type(message_0.start_position).__qualname__}"
        == "base.Position"
    )
    assert (
        f"{type(message_0.end_position).__module__}.{type(message_0.end_position).__qualname__}"
        == "base.Position"
    )
    int_0 = message_0.__hash__()
    assert int_0 == -2590049272368845124
    bool_1 = message_0.__eq__(int_0)
    assert bool_1 is False
    module_0.ParseError(code=none_type_1, messages=none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_41():
    none_type_0 = None
    validation_result_0 = module_0.ValidationResult()
    position_0 = module_0.Position(
        validation_result_0, validation_result_0, none_type_0
    )
    none_type_1 = None
    message_0 = module_0.Message(
        text=none_type_1, position=none_type_0, start_position=validation_result_0
    )
    assert (
        f"{type(message_0).__module__}.{type(message_0).__qualname__}" == "base.Message"
    )
    assert message_0.text is None
    assert message_0.code == "custom"
    assert message_0.index == []
    assert (
        f"{type(message_0.start_position).__module__}.{type(message_0.start_position).__qualname__}"
        == "base.ValidationResult"
    )
    assert message_0.end_position is None
    int_0 = message_0.__hash__()
    assert int_0 == -3236363584314578347
    message_1 = module_0.Message(text=none_type_1, key=none_type_0)
    assert message_1.code == "custom"
    assert message_1.index == []
    bool_0 = message_1.__eq__(message_0)
    assert bool_0 is False
    parse_error_0 = module_0.ParseError(text=bool_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    var_0 = parse_error_0.__eq__(none_type_0)
    assert var_0 is False
    var_0.messages()


def test_case_42():
    none_type_0 = None
    validation_result_0 = module_0.ValidationResult()
    bool_0 = True
    position_0 = module_0.Position(bool_0, bool_0, none_type_0)
    none_type_1 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(text=str_0, end_position=none_type_0)
    assert message_0.code == "custom"
    assert message_0.index == []
    int_0 = message_0.__hash__()
    assert int_0 == -3236363584314578347
    bool_1 = message_0.__eq__(position_0)
    assert bool_1 is False
    list_0 = [message_0, message_0, message_0, message_0]
    parse_error_0 = module_0.ParseError(code=none_type_1, messages=list_0)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    list_1 = parse_error_0.messages()
    str_1 = message_0.__repr__()
    assert str_1 == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom')"
    bool_2 = position_0.__eq__(str_0)
    assert bool_2 is False
    str_2 = parse_error_0.__repr__()
    assert (
        str_2
        == "ParseError([Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom'), Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom'), Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom'), Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom')])"
    )
    str_3 = parse_error_0.__str__()
    assert str_3 == "{'': 'cfPI`g:CXV\\x0cS\\tI'}"
    str_4 = position_0.__repr__()
    assert str_4 == "Position(line_no=True, column_no=True, char_index=None)"
    bool_3 = position_0.__eq__(str_2)
    str_5 = parse_error_0.__repr__()
    assert (
        str_5
        == "ParseError([Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom'), Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom'), Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom'), Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom')])"
    )
    var_0 = parse_error_0.values()
    assert len(var_0) == 1
    bool_4 = position_0.__eq__(var_0)
    with pytest.raises(AssertionError):
        module_0.BaseError(key=none_type_0, position=position_0)


@pytest.mark.xfail(strict=True)
def test_case_43():
    none_type_0 = None
    position_0 = module_0.Position(none_type_0, none_type_0, none_type_0)
    none_type_1 = None
    str_0 = "cfPI`g:CXV\x0cS\tI"
    message_0 = module_0.Message(
        text=str_0, key=str_0, position=str_0, start_position=none_type_1
    )
    assert message_0.code == "custom"
    assert message_0.index == ["cfPI`g:CXV\x0cS\tI"]
    assert message_0.start_position == "cfPI`g:CXV\x0cS\tI"
    assert message_0.end_position == "cfPI`g:CXV\x0cS\tI"
    int_0 = message_0.__hash__()
    assert int_0 == 5322473327714082801
    bool_0 = message_0.__eq__(message_0)
    assert bool_0 is True
    parse_error_0 = module_0.ParseError(text=str_0, position=none_type_1)
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "base.ParseError"
    )
    assert len(parse_error_0) == 1
    iterator_0 = parse_error_0.__iter__()
    validation_result_0 = module_0.ValidationResult(value=message_0)
    assert (
        f"{type(validation_result_0).__module__}.{type(validation_result_0).__qualname__}"
        == "base.ValidationResult"
    )
    assert (
        f"{type(validation_result_0.value).__module__}.{type(validation_result_0.value).__qualname__}"
        == "base.Message"
    )
    assert validation_result_0.error is None
    var_0 = parse_error_0.__eq__(str_0)
    assert var_0 is False
    int_1 = var_0.__hash__()
    assert int_1 == 0
    list_0 = parse_error_0.messages()
    str_1 = message_0.__repr__()
    assert (
        str_1
        == "Message(text='cfPI`g:CXV\\x0cS\\tI', code='custom', index=['cfPI`g:CXV\\x0cS\\tI'], position='cfPI`g:CXV\\x0cS\\tI')"
    )
    bool_1 = parse_error_0.__eq__(list_0)
    assert bool_1 is False
    str_2 = parse_error_0.__repr__()
    assert str_2 == "ParseError(text='cfPI`g:CXV\\x0cS\\tI', code='custom')"
    position_1 = module_0.Position(none_type_0, bool_1, var_0)
    assert position_1.column_no is False
    assert position_1.char_index is False
    bool_2 = position_0.__eq__(position_1)
    assert bool_2 is False
    str_3 = parse_error_0.__str__()
    assert str_3 == "cfPI`g:CXV\x0cS\tI"
    str_4 = var_0.__repr__()
    assert str_4 == "False"
    bool_3 = position_0.__eq__(position_0)
    assert bool_3 is True
    bool_4 = True
    bool_5 = position_0.__eq__(bool_4)
    assert bool_5 is False
    module_0.BaseError(key=none_type_1, messages=message_0)
