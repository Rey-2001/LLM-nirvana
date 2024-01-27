
import pytest
from schemas import Schema, Field, Array, Object, ValidationError, Reference, SchemaDefinitions

def test_schema_with_required_fields():
    class MySchema(Schema):
        name = Field(required=True)
        age = Field(required=True)

    # Valid input
    data = {"name": "John", "age": 25}
    schema = MySchema(data)
    assert schema["name"] == "John"
    assert schema["age"] == 25
    
    # Missing required field "name"
    with pytest.raises(ValidationError):
        MySchema.validate_or_error({"age": 25})

    # Missing required field "name" and extra field "address"
    with pytest.raises(ValidationError):
        MySchema.validate_or_error({"age": 25, "address": "123 Street"})

def test_schema_with_default_values():
    class MySchema(Schema):
        name = Field(default="John")
        age = Field(default=25)
        address = Field(default="")

    # Valid input with missing fields
    data = {}
    schema = MySchema(data)
    assert schema["name"] == "John"
    assert schema["age"] == 25
    assert schema["address"] == ""

    # Valid input with provided values
    data = {"name": "Alice", "age": 30, "address": "123 Street"}
    schema = MySchema(data)
    assert schema["name"] == "Alice"
    assert schema["age"] == 30
    assert schema["address"] == "123 Street"

def test_schema_with_nested_fields():
    class AddressSchema(Schema):
        street = Field(required=True)
        city = Field(required=True)
        state = Field(required=True)

    class PersonSchema(Schema):
        name = Field(required=True)
        age = Field(required=True)
        address = Object(AddressSchema)

    # Valid input with nested fields
    data = {
        "name": "John",
        "age": 25,
        "address": {
            "street": "123 Street",
            "city": "New York",
            "state": "NY"
        }
    }
    schema = PersonSchema(data)
    assert schema["name"] == "John"
    assert schema["age"] == 25
    assert isinstance(schema["address"], AddressSchema)
    assert schema["address"]["street"] == "123 Street"
    assert schema["address"]["city"] == "New York"
    assert schema["address"]["state"] == "NY"

    # Missing nested required field "street"
    with pytest.raises(ValidationError):
        PersonSchema.validate_or_error({
            "name": "John",
            "age": 25,
            "address": {
                "city": "New York",
                "state": "NY"
            }
        })

def test_schema_with_array_field():
    class MySchema(Schema):
        tags = Array(Field())

    # Valid input with array field
    data = {"tags": ["red", "green", "blue"]}
    schema = MySchema(data)
    assert schema["tags"] == ["red", "green", "blue"]

    # Valid input with empty array
    data = {"tags": []}
    schema = MySchema(data)
    assert schema["tags"] == []

    # Invalid input with non-array value
    with pytest.raises(ValidationError):
        MySchema.validate_or_error({"tags": "red"})

def test_schema_with_reference_field():
    class UserSchema(Schema):
        name = Field(required=True)
        age = Field(required=True)

    class PostSchema(Schema):
        title = Field(required=True)
        author = Reference(to=UserSchema)

    # Valid input with reference field
    data = {
        "title": "First Post",
        "author": {"name": "John Doe", "age": 30}
    }
    schema = PostSchema(data)
    assert schema["title"] == "First Post"
    assert isinstance(schema["author"], UserSchema)
    assert schema["author"]["name"] == "John Doe"
    assert schema["author"]["age"] == 30

    # Missing required field "title" in reference field
    with pytest.raises(ValidationError):
        PostSchema.validate_or_error({"author": {"name": "John Doe", "age": 30}})
