import pytest
from base import Position, Message, BaseError, ValidationError, ValidationResult


def test_position_equal():
    position1 = Position(line_no=1, column_no=2, char_index=3)
    position2 = Position(line_no=1, column_no=2, char_index=3)
    assert position1 == position2


def test_position_not_equal():
    position1 = Position(line_no=1, column_no=2, char_index=3)
    position2 = Position(line_no=1, column_no=2, char_index=4)
    assert position1 != position2


def test_message_eq():
    message1 = Message(text="Error message", code="error_code")
    message2 = Message(text="Error message", code="error_code")
    assert message1 == message2


def test_message_neq():
    message1 = Message(text="Error message", code="error_code")
    message2 = Message(text="Different error message", code="error_code")
    assert message1 != message2


def test_error_eq():
    error1 = BaseError(text="Error message")
    error2 = BaseError(text="Error message")
    assert error1 == error2


def test_error_neq():
    error1 = BaseError(text="Error message 1")
    error2 = BaseError(text="Error message 2")
    assert error1 != error2


def test_validation_result_bool():
    result1 = ValidationResult(value=["a", "b", "c"])
    result2 = ValidationResult(error=ValidationError(text="Invalid data"))
    assert bool(result1) is True
    assert bool(result2) is False


def test_validation_result_repr():
    result1 = ValidationResult(value=["a", "b", "c"])
    result2 = ValidationResult(error=ValidationError(text="Invalid data"))
    assert repr(result1) == "ValidationResult(value=['a', 'b', 'c'])"
    assert repr(result2) == "ValidationResult(error=ValidationError(text='Invalid data'))"