import pytest
from programs import factorial

def test_factorial_zero():
    assert factorial.fact(0) == 1

def test_factorial_value():
    assert factorial.fact(4) == 24

def test_factorial_float():
    assert factorial.fact(0.0) == 1.0