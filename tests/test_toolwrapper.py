import pytest
import toolwrapper


# it is likely that some of these tests will not pass on windows
# because some of the external programs are not installed


sample_lines = [
    "hello",
    "hello again",
    "good bye"
]


def test_toolwrapper():
    with toolwrapper.ToolWrapper(["cat"]) as cat:
        for line in sample_lines:
            cat.writeline(line)
            assert cat.readline() == line


def test_toolwrapper_no_stdbuf():
    with toolwrapper.ToolWrapper(["cat"], stdbuf=False) as cat:
        for line in sample_lines:
            cat.writeline(line)
            assert cat.readline() == line


def test_toolwrapper_repr():
    x = toolwrapper.ToolWrapper(["a", "b"], start=False, cwd="d")
    assert repr(x) == '''ToolWrapper(['a', 'b'], encoding='utf-8', cwd='d')'''


def test_toolwrapper_str():
    x = toolwrapper.ToolWrapper(["a", "b"])
    assert str(x) == '''ToolWrapper'''


def test_toolwrapper_start_stop_restart():
    tool = toolwrapper.ToolWrapper(["cat"], start=False)
    assert tool.proc is None
    tool.start()
    pid = tool.proc.pid
    with pytest.raises(toolwrapper.ToolException):
        tool.start()
    tool.close()
    assert tool.closed
    tool.start()
    assert pid != tool.proc.pid
    pid = tool.proc.pid
    tool.restart()
    assert pid != tool.proc.pid
    tool.close()


def test_toolwrapper_read_write_when_closed():
    tool = toolwrapper.ToolWrapper(["cat"], start=False)
    with pytest.raises(toolwrapper.ToolException):
        tool.writeline("hello")
    with pytest.raises(toolwrapper.ToolException):
        tool.readline()
    tool.start()
    tool.writeline("hello")
    assert "hello" == tool.readline()
    tool.close()
    with pytest.raises(toolwrapper.ToolException):
        tool.writeline("hello")
    with pytest.raises(toolwrapper.ToolException):
        tool.readline()


