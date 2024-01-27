import manipulation

def test_reverse():
    assert manipulation.reverse("hello") == "olleh"
    assert manipulation.reverse("123456") == "654321"
    assert manipulation.reverse("!dlroW olleH") == "Hello World!"

def test_camel_case_to_snake():
    assert manipulation.camel_case_to_snake("ThisIsACamelStringTest") == "this_is_a_camel_case_string_test"
    assert manipulation.camel_case_to_snake("HelloWorld") == "hello_world"
    assert manipulation.camel_case_to_snake("oneTwoThreeFour") == "one_two_three_four"

def test_snake_case_to_camel():
    assert manipulation.snake_case_to_camel("the_snake_is_green") == "TheSnakeIsGreen"
    assert manipulation.snake_case_to_camel("apple_tree") == "AppleTree"
    assert manipulation.snake_case_to_camel("this_is_an_manipulation") == "ThisIsAnmanipulation"

def test_shuffle():
    assert len(manipulation.shuffle("hello world")) == 11
    assert len(manipulation.shuffle("123456789")) == 9
    assert manipulation.shuffle("shuffle") != "shuffle"

def test_strip_html():
    assert manipulation.strip_html("<p>Hello World</p>") == "Hello World"
    assert manipulation.strip_html("<a href='manipulation.com'>Click here</a>") == "Click here"

def test_prettify():
    assert manipulation.prettify(" unprettified string ,, like this one,will be\"prettified\" .th' s awesome! ") == "Unprettified string, like this one, will be \"prettified\". It's awesome!"
    assert manipulation.prettify("   hello    world    ") == "Hello World"

def test_asciify():
    assert manipulation.asciify("èéùúòóäåëýñÅÀÁÇÌÍÑÓË") == "eeuuooaaeyn"
    assert manipulation.asciify("Mönstér Mägnët") == "Monster Magnet"

def test_slugify():
    assert manipulation.slugify("Top 10 Reasons To Love Dogs!!!") == "top-10-reasons-to-love-dogs"
    assert manipulation.slugify("Mönstér Mägnët") == "monster-magnet"

def test_booleanize():
    assert manipulation.booleanize("true") == True
    assert manipulation.booleanize("FALSE") == False
    assert manipulation.booleanize("yes") == True

def test_strip_margin():
    input_string = """
    This is a
    multi line
    string
    """
    expected_output = "This is a\nmulti line\nstring"
    assert manipulation.strip_margin(input_string) == expected_output

def test_compress():
    assert len(manipulation.compress("hello world")) < len("hello world")
    assert len(manipulation.compress("1234567890")) < len("1234567890")
    assert len(manipulation.compress(" " * 1024) > len(" " * 1024))

def test_decompress():
    assert manipulation.decompress(manipulation.compress("hello world")) == "hello world"
    assert manipulation.decompress(manipulation.compress("1234567890")) == "1234567890"
    assert manipulation.decompress(manipulation.compress(" " * 1024)) == " " * 1024

def test_roman_encode():
    assert manipulation.roman_encode(37) == "XXXVII"
    assert manipulation.roman_encode("2020") == "MMXX"
    assert manipulation.roman_encode(3999) == "MMMCMXCIX"

def test_roman_decode():
    assert manipulation.roman_decode("VII") == 7
    assert manipulation.roman_decode("XLV") == 45
    assert manipulation.roman_decode("MMXX") == 2020
