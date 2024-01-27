import pytest
from monad_try import Try

def test_try_of_success():
    value = Try.of(lambda: 10)
    assert value == Try(10, True)

def test_try_of_failure():
    value = Try.of(lambda: 1/0)
    assert value == Try(ZeroDivisionError('division by zero'), False)

def test_try_map_success():
    value = Try.of(lambda: 10).map(lambda x: x * 2)
    assert value == Try(20, True)

def test_try_map_failure():
    value = Try.of(lambda: 1/0).map(lambda x: x * 2)
    assert value == Try(ZeroDivisionError('division by zero'), False)

def test_try_bind_success():
    value = Try.of(lambda: 10).bind(lambda x: Try.of(lambda: x * 2))
    assert value == Try(20, True)

def test_try_bind_failure():
    value = Try.of(lambda: 1/0).bind(lambda x: Try.of(lambda: x * 2))
    assert value == Try(ZeroDivisionError('division by zero'), False)

def test_try_on_success():
    success_callback = []

    def callback(x):
        success_callback.append(x)

    value = Try.of(lambda: 10).on_success(callback)
    assert value == Try(10, True)
    assert success_callback == [10]

def test_try_on_fail():
    fail_callback = []

    def callback(x):
        fail_callback.append(x)

    value = Try.of(lambda: 1/0).on_fail(callback)
    assert value == Try(ZeroDivisionError('division by zero'), False)
    assert fail_callback == [ZeroDivisionError('division by zero')]

def test_try_filter_success():
    value = Try.of(lambda: 10).filter(lambda x: x > 5)
    assert value == Try(10, True)

def test_try_filter_failure():
    value = Try.of(lambda: 10).filter(lambda x: x < 5)
    assert value == Try(10, False)

def test_try_get():
    value = Try.of(lambda: 10).get()
    assert value == 10

def test_try_get_or_else_success():
    value = Try.of(lambda: 10).get_or_else(0)
    assert value == 10

def test_try_get_or_else_failure():
    value = Try.of(lambda: 1/0).get_or_else(0)
    assert value == 0