import pytest
from _timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_add(timers):
    timers.add("timer1", 1.5)
    assert timers.data["timer1"] == 1.5
    assert timers._timings["timer1"] == [1.5]

def test_clear(timers):
    timers.add("timer1", 1.5)
    timers.clear()
    assert timers.data == {}
    assert timers._timings == {}

def test_count(timers):
    timers.add("timer1", 1.5)
    timers.add("timer1", 2.0)
    assert timers.count("timer1") == 2

def test_total(timers):
    timers.add("timer1", 1.5)
    timers.add("timer1", 2.0)
    assert timers.total("timer1") == 3.5

def test_min(timers):
    timers.add("timer1", 1.5)
    timers.add("timer1", 2.0)
    assert timers.min("timer1") == 1.5

def test_max(timers):
    timers.add("timer1", 1.5)
    timers.add("timer1", 2.0)
    assert timers.max("timer1") == 2.0

def test_mean(timers):
    timers.add("timer1", 1.5)
    timers.add("timer1", 2.5)
    assert timers.mean("timer1") == 2.0

def test_median(timers):
    timers.add("timer1", 1.5)
    timers.add("timer1", 2.5)
    assert timers.median("timer1") == 2.0

def test_stdev(timers):
    timers.add("timer1", 1.5)
    assert timers.stdev("timer1") == 0.0
    
    timers.add("timer1", 2.5)
    assert timers.stdev("timer1") == pytest.approx(0.7071)