
import pytest
from api import LetterCase, DataClassJsonMixin, dataclass_json

@dataclass_json
class Person(DataClassJsonMixin):
    name: str
    age: int

def test_to_json():
    person = Person(name="John Doe", age=25)
    assert person.to_json() == '{"name": "John Doe", "age": 25}'

def test_from_json():
    json_str = '{"name": "John Doe", "age": 25}'
    person = Person.from_json(json_str)
    assert person.name == "John Doe"
    assert person.age == 25

def test_to_dict():
    person = Person(name="John Doe", age=25)
    assert person.to_dict() == {'name': 'John Doe', 'age': 25}

def test_from_dict():
    person_dict = {'name': 'John Doe', 'age': 25}
    person = Person.from_dict(person_dict)
    assert person.name == "John Doe"
    assert person.age == 25

def test_schema():
    schema = Person.schema()
    assert schema.dump(Person(name="John Doe", age=25)) == {"name": "John Doe", "age": 25}

def test_letter_case():
    @dataclass_json(letter_case=LetterCase.CAMEL.value)
    class SnakeCaseDataClass(DataClassJsonMixin):
        snake_case: str

    snake_case_obj = SnakeCaseDataClass(snake_case="Hello")
    assert snake_case_obj.to_dict() == {'snakeCase': 'Hello'}
    assert snake_case_obj.to_json() == '{"snakeCase": "Hello"}'

def test_undefined():
    @dataclass_json(undefined="ignore")
    class UndefinedDataClass(DataClassJsonMixin):
        undefined_val: str

    undefined_obj = UndefinedDataClass(undefined_val="Hello")
    assert undefined_obj.to_dict() == {'undefined_val': 'Hello'}
    assert undefined_obj.to_json() == '{"undefined_val": "Hello"}'

def test_partial():
    @dataclass_json
    class api(DataClassJsonMixin):
        name: str
        age: int
        gender: str

    api = api(name="John Doe", age=25, gender="Male")
    partial_schema = api.schema(partial=True)
    assert partial_schema.load({"name": "Jane Doe"}) == api(name="Jane Doe", age=25, gender="Male")

