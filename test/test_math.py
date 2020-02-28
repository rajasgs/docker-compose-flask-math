import pytest

def add(a, b):

    return a + b

def test_math():
    
    a = 1
    b = 2

    assert add(a, b) == 3
