#Here are the pytest unit test cases for the given code:

import txtutils

def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert txtutils.len_without_ansi(text) == 6

def test_AnsiTextWrapper_wrap():
    wrapper = txtutils.AnsiTextWrapper(width=10)
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    expected_output = [
        'Lorem',
        'ipsum',
        'dolor sit',
        'amet,',
        'consectetur',
        'adipiscing',
        'elit.'
    ]
    assert wrapper.wrap(text) == expected_output

def test_AnsiTextWrapper_fill():
    wrapper = txtutils.AnsiTextWrapper(width=10)
    text = 'Lorem ipsum dolor sit amet, consectetur'