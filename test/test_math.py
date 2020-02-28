import pytest

import math_util

def test_math_add():
    
    a = 1
    b = 2

    assert math_util.add(a, b) == 3

def test_math_subtract():
    
    a = 10
    b = 2

    assert math_util.subtract(a, b) == 8
