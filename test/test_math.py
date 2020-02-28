import pytest

def add(a, b):

    return a + b

def test_math():
    params = {
        'a' : 1,
        'b' : 2
    }
    assert add(params) == 3
