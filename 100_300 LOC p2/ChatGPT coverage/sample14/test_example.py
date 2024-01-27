import pytest
from either import Either, Left, Right


def test_either_case_left():
    def error(x):
        return x + 1

    def success(x):
        return x * 2

    either = Left(5)
    result = either.case(error, success)

    assert result == 6


def test_either_case_right():
    def error(x):
        return x + 1

    def success(x):
        return x * 2

    either = Right(5)
    result = either.case(error, success)

    assert result == 10


def test_left_map():
    def mapper(x):
        return x * 2

    left = Left(5)
    result = left.map(mapper)

    assert result == Left(5)


def test_left_bind():
    def mapper(x):
        return Left(x + 1)

    left = Left(5)
    result = left.bind(mapper)

    assert result == left


def test_left_is_left():
    left = Left(5)
    result = left.is_left()

    assert result is True


def test_left_is_right():
    left = Left(5)
    result = left.is_right()

    assert result is False


def test_left_to_maybe():
    left = Left(5)
    result = left.to_maybe()

    assert result.is_nothing()


def test_left_to_validation():
    left = Left(5)
    result = left.to_validation()

    assert result.is_fail()
    assert result.value == [5]


def test_right_map():
    def mapper(x):
        return x * 2

    right = Right(5)
    result = right.map(mapper)

    assert result == Right(10)


def test_right_bind():
    def mapper(x):
        return Right(x + 1)

    right = Right(5)
    result = right.bind(mapper)

    assert result == Right(6)


def test_right_is_right():
    right = Right(5)
    result = right.is_right()

    assert result is True


def test_right_is_left():
    right = Right(5)
    result = right.is_left()

    assert result is False


def test_right_to_maybe():
    right = Right(5)
    result = right.to_maybe()

    assert result.is_just()
    assert result.value == 5


def test_right_to_validation():
    right = Right(5)
    result = right.to_validation()

    assert result.is_success()
    assert result.value == 5