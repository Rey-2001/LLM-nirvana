# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import example as module_0


def test_case_0():
    str_0 = "lEh+W6c@twJ"
    var_0 = module_0.truncate(str_0)
    assert var_0 == "lEh+W6c@twJ"
    assert module_0.ROW_FMT == "{{:<{1}}} | {{:<{2}}} | {{:{0}{3}}}"


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.format_entries(none_type_0, none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "lEh+W6c@twJ"
    module_0.create_entry(str_0, str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"8J\x8d\x8fLwJ$\xbd\x9a\x9b\xaf\\T"
    bool_0 = False
    module_0.truncate(bytes_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "en_US"
    module_0.format_entries(str_0, str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "nl_NL"
    module_0.LCInfo(str_0, str_0, str_0)