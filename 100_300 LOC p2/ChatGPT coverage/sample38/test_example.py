
import pytest
from datetime import datetime
from decimal import Decimal
from enum import Enum
from uuid import UUID

from core import (_asdict, _decode_dataclass, _decode_generic,
                     _encode_overrides, _is_supported_generic, _support_extended_types)


class MyEnum(Enum):
    VALUE1 = 1
    VALUE2 = 2
    VALUE3 = 3


class MyDataClass:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value


class Testcore:
    def test_asdict_dataclass(self):
        obj = MyDataClass("test", 100)
        expected = {"name": "test", "value": 100}
        assert _asdict(obj) == expected

    def test_asdict_mapping(self):
        obj = {"key1": "value1", "key2": 123}
        expected = {"key1": "value1", "key2": 123}
        assert _asdict(obj) == expected

    def test_asdict_collection(self):
        obj = [1, 2, 3]
        expected = [1, 2, 3]
        assert _asdict(obj) == expected

    def test_asdict_nested(self):
        obj = {
            "key1": MyDataClass("test", 100),
            "key2": {"nested": "value"},
            "key3": [1, 2, 3]
        }
        expected = {
            "key1": {"name": "test", "value": 100},
            "key2": {"nested": "value"},
            "key3": [1, 2, 3]
        }
        assert _asdict(obj) == expected

    def test_decode_dataclass(self):
        data = {"name": "test", "value": 100}
        expected = MyDataClass("test", 100)
        assert _decode_dataclass(MyDataClass, data) == expected

    def test_decode_generic_list(self):
        data = [1, 2, 3]
        expected = [1, 2, 3]
        assert _decode_generic(list, data) == expected

    def test_decode_generic_dict(self):
        data = {"key1": "value1", "key2": 123}
        expected = {"key1": "value1", "key2": 123}
        assert _decode_generic(dict, data) == expected

    def test_is_supported_generic_true(self):
        assert _is_supported_generic(list) is True
        assert _is_supported_generic(dict) is True
        assert _is_supported_generic(set) is True
        assert _is_supported_generic(tuple) is True
        assert _is_supported_generic(str) is False
        assert _is_supported_generic(bytes) is False
        assert _is_supported_generic(int) is False

    def test_support_extended_types(self):
        assert _support_extended_types(int, 10) == 10
        assert _support_extended_types(str, "test") == "test"
        assert _support_extended_types(float, 3.14) == 3.14
        assert _support_extended_types(bool, True) is True
        assert _support_extended_types(Decimal, "10.5") == Decimal("10.5")
        assert _support_extended_types(datetime, datetime.now()) == datetime.now()
        assert _support_extended_types(UUID, "123e4567-e89b-12d3-a456-426614174000") == UUID("123e4567-e89b-12d3-a456-426614174000")
        assert _support_extended_types(MyEnum, "VALUE1") == MyEnum.VALUE1


if __name__ == "__main__":
    pytest.main()
