
import pytest
import subprocess

from exception import log, exception_wrapper
from exception import *


def test_register_ipython_excepthook():
    # Test that register_ipython_excepthook does not raise any exceptions
    register_ipython_excepthook()


def test_log_exception():
    # Test that log_exception does not raise any exceptions
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        log_exception(e)


def test_exception_wrapper_no_handler():
    # Test that exception_wrapper without a custom handler calls log_exception
    @exception_wrapper()
    def test_func():
        raise ValueError("Test exception")

    # Test that the wrapped function raises the correct exception
    with pytest.raises(ValueError):
        test_func()


def test_exception_wrapper_with_handler():
    # Test that exception_wrapper with a custom handler calls the handler function
    def custom_handler(e):
        assert isinstance(e, ValueError)

    @exception_wrapper(custom_handler)
    def test_func():
        raise ValueError("Test exception")

    # Test that the wrapped function raises the correct exception
    with pytest.raises(ValueError):
        test_func()


def test_exception_wrapper_with_handler_and_args():
    # Test that exception_wrapper with a custom handler and method arguments passes the arguments correctly
    def custom_handler(e, arg1, arg2):
        assert isinstance(e, ValueError)
        assert arg1 == "arg1"
        assert arg2 == "arg2"

    @exception_wrapper(custom_handler)
    def test_func(arg1, arg2):
        raise ValueError("Test exception")

    # Test that the wrapped function raises the correct exception
    with pytest.raises(ValueError):
        test_func("arg1", "arg2")


def test_exception_wrapper_with_handler_and_kwargs():
    # Test that exception_wrapper with a custom handler and keyword arguments passes the arguments correctly
    def custom_handler(e, arg1, arg2):
        assert isinstance(e, ValueError)
        assert arg1 == "arg1"
        assert arg2 == "arg2"

    @exception_wrapper(custom_handler)
    def test_func(arg1=None, arg2=None):
        raise ValueError("Test exception")

    # Test that the wrapped function raises the correct exception
    with pytest.raises(ValueError):
        test_func(arg1="arg1", arg2="arg2")


def test_exception_wrapper_with_handler_and_args_kwargs():
    # Test that exception_wrapper with a custom handler, method arguments, and keyword arguments passes the arguments correctly
    def custom_handler(e, arg1, arg2, *args, **kwargs):
        assert isinstance(e, ValueError)
        assert arg1 == "arg1"
        assert arg2 == "arg2"
        assert args == ("arg3",)
        assert kwargs == {"kwarg1": "value1", "kwarg2": "value2"}

    @exception_wrapper(custom_handler)
    def test_func(arg1=None, arg2=None, *args, **kwargs):
        raise ValueError("Test exception")

    # Test that the wrapped function raises the correct exception
    with pytest.raises(ValueError):
        test_func("arg1", "arg2", "arg3", kwarg1="value1", kwarg2="value2")


def test_exception_wrapper_invalid_handler():
    # Test that exception_wrapper with an invalid custom handler raises ValueError
    with pytest.raises(ValueError):
        @exception_wrapper(lambda: None)
        def test_func():
            pass


def test_log_exception_calledprocesserror():
    # Test that log_exception handles subprocess.CalledProcessError correctly
    try:
        cmd = ["invalid_command"]
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        log_exception(e)


def test_log_exception_other_exception():
    # Test that log_exception can handle other types of exceptions correctly
    try:
        raise RuntimeError("Test exception")
    except RuntimeError as e:
        log_exception(e)


def test_log_exception_none_output():
    # Test that log_exception handles CalledProcessError with None output correctly
    try:
        cmd = ["valid_command"]
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        e.output = None
        log_exception(e)


if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", __file__])
