# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import run as module_0


def test_case_0():
    none_type_0 = None
    var_0 = module_0.error_wrapper(none_type_0)
    assert module_0.MAX_OUTPUT_LENGTH == 8192


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 2022
    module_0.run_command(int_0, ignore_errors=int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xe1N\xfd\xd8\x1c\xf0\xd4Q\xae$jW\xea\x8a\x98"
    module_0.run_command(bytes_0, cwd=bytes_0, verbose=bytes_0, return_output=bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.CommandResult()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "nNr=V.,cT"
    module_0.run_command(str_0, verbose=str_0)


def test_case_5():
    str_0 = "CC"
    str_1 = "xSyUmyq8i=UjrvWEX%c"
    list_0 = [
        str_0,
        str_0,
        str_1,
        str_0,
        str_0,
        str_0,
        str_1,
        str_0,
        str_0,
        str_1,
        str_0,
        str_1,
        str_1,
    ]
    var_0 = module_0.error_wrapper(str_0)
    assert var_0 == "CC"
    assert module_0.MAX_OUTPUT_LENGTH == 8192
    none_type_0 = None
    module_0.run_command(list_0, env=none_type_0, return_output=var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "CC"
    var_0 = module_0.error_wrapper(str_0)
    assert var_0 == "CC"
    assert module_0.MAX_OUTPUT_LENGTH == 8192
    command_result_0 = module_0.run_command(var_0, ignore_errors=var_0)
    assert (
        f"{type(command_result_0).__module__}.{type(command_result_0).__qualname__}"
        == "run.CommandResult"
    )
    assert len(command_result_0) == 3
    var_1 = module_0.error_wrapper(str_0)
    module_0.run_command(str_0, cwd=str_0, ignore_errors=str_0, **str_0)