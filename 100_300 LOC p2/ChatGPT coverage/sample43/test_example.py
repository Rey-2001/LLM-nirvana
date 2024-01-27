import pytest

from run import run_command, CommandResult

def test_run_command():
    # Test with a single string as args
    result = run_command("echo Hello, World!")
    assert isinstance(result, CommandResult)
    assert result.return_code == 0
    assert result.captured_output == b"Hello, World!\n"

    # Test with a list of strings as args
    result = run_command(["echo", "Hello,", "World!"])
    assert isinstance(result, CommandResult)
    assert result.return_code == 0
    assert result.captured_output == b"Hello, World!\n"

    # Test with env and cwd specified
    result = run_command("pwd", env={"VAR": "value"}, cwd="/path/to/dir")
    assert isinstance(result, CommandResult)
    assert result.return_code == 0
    assert result.captured_output == b"/path/to/dir\n"

    # Test with timeout specified
    result = run_command("sleep 1", timeout=0.5, ignore_errors=True)
    assert isinstance(result, CommandResult)
    assert result.return_code == -32768  # special return code for subprocess.TimeoutExpired
    assert result.captured_output is not None

    # Test with return_output enabled
    result = run_command("echo Hello, World!", return_output=True)
    assert isinstance(result, CommandResult)
    assert result.return_code == 0
    assert result.captured_output == b"Hello, World!\n"

    # Test with ignore_errors enabled
    result = run_command("command_not_found", ignore_errors=True)
    assert isinstance(result, CommandResult)
    assert result.return_code != 0
    assert result.captured_output is not None

    # Test with verbose enabled
    result = run_command("echo Hello, World!", verbose=True)
    assert isinstance(result, CommandResult)
    assert result.return_code == 0
    assert result.captured_output == b"Hello, World!\n"