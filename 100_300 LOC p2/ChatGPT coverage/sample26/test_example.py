import pytest
import datetime
from formats import DateFormat, TimeFormat, DateTimeFormat, UUIDFormat
from formats import *

def test_date_format_native_type():
    formatter = DateFormat()
    assert formatter.is_native_type(datetime.date.today()) == True
    assert formatter.is_native_type(datetime.datetime.now()) == False

def test_date_format_valid_date():
    formatter = DateFormat()
    assert formatter.validate("2021-09-01") == datetime.date(2021, 9, 1)
    assert formatter.validate("2021-01-01") == datetime.date(2021, 1, 1)

def test_date_format_invalid_date():
    formatter = DateFormat()
    with pytest.raises(formatter.validation_error("invalid")):
        formatter.validate("2022-02-30")
    with pytest.raises(formatter.validation_error("invalid")):
        formatter.validate("2022-12-32")

def test_date_format_serialize():
    formatter = DateFormat()
    assert formatter.serialize(datetime.date(2021, 9, 1)) == "2021-09-01"
    assert formatter.serialize(None) == None


def test_time_format_native_type():
    formatter = TimeFormat()
    assert formatter.is_native_type(datetime.time()) == True
    assert formatter.is_native_type(datetime.datetime.now()) == False

def test_time_format_valid_time():
    formatter = TimeFormat()
    assert formatter.validate("12:34") == datetime.time(12, 34)
    assert formatter.validate("12:34:56") == datetime.time(12, 34, 56)
    assert formatter.validate("12:34:56.789") == datetime.time(12, 34, 56, 789000)

def test_time_format_invalid_time():
    formatter = TimeFormat()
    with pytest.raises(formatter.validation_error("invalid")):
        formatter.validate("25:00")
    with pytest.raises(formatter.validation_error("invalid")):
        formatter.validate("12:60")
    with pytest.raises(formatter.validation_error("invalid")):
        formatter.validate("12:34:56.7890")

def test_time_format_serialize():
    formatter = TimeFormat()
    assert formatter.serialize(datetime.time(12, 34, 56)) == "12:34:56"
    assert formatter.serialize(None) == None


def test_datetime_format_native_type():
    formatter = DateTimeFormat()
    assert formatter.is_native_type(datetime.datetime.now()) == True
    assert formatter.is_native_type(datetime.date.today()) == False

def test_datetime_format_valid_datetime():
    formatter = DateTimeFormat()
    assert formatter.validate("2021-09-01T12:34:56") == datetime.datetime(2021, 9, 1, 12, 34, 56)
    assert formatter.validate("2021-09-01T12:34:56.789") == datetime.datetime(2021, 9, 1, 12, 34, 56, 789000)
    assert formatter.validate("2022-12-31 23:59:59") == datetime.datetime(2022, 12, 31, 23, 59, 59)
    assert formatter.validate("2022-12-31T23:59:59.999") == datetime.datetime(2022, 12, 31, 23, 59, 59, 999000)

def test_datetime_format_invalid_datetime():
    formatter = DateTimeFormat()
    with pytest.raises(formatter.validation_error("invalid")):
        formatter.validate("2022-02-30T12:34:56")
    with pytest.raises(formatter.validation_error("invalid")):
        formatter.validate("2022-12-32T12:34:56")
    with pytest.raises(formatter.validation_error("invalid")):
        formatter.validate("2022-02-28T12:34:56.7890")

def test_datetime_format_serialize():
    formatter = DateTimeFormat()
    assert formatter.serialize(datetime.datetime(2021, 9, 1, 12, 34, 56)) == "2021-09-01T12:34:56"
    assert formatter.serialize(None) == None


def test_uuid_format_native_type():
    formatter = UUIDFormat()
    assert formatter.is_native_type(uuid.UUID()) == True
    assert formatter.is_native_type("123e4567-e89b-12d3-a456-426655440000") == False

def test_uuid_format_valid_uuid():
    formatter = UUIDFormat()
    assert formatter.validate("123e4567-e89b-12d3-a456-426655440000") == uuid.UUID("123e4567-e89b-12d3-a456-426655440000")
    assert formatter.validate("00000000-0000-0000-0000-000000000000") == uuid.UUID("00000000-0000-0000-0000-000000000000")

def test_uuid_format_invalid_uuid():
    formatter = UUIDFormat()
    with pytest.raises(formatter.validation_error("format")):
        formatter.validate("1234567890")
    with pytest.raises(formatter.validation_error("format")):
        formatter.validate("abcdefab-abcd-abcd-abcd-abcdefabcdef")

def test_uuid_format_serialize():
    formatter = UUIDFormat()
    assert formatter.serialize(uuid.UUID("123e4567-e89b-12d3-a456-426655440000")) == "123e4567-e89b-12d3-a456-426655440000"
    assert formatter.serialize(None) == None