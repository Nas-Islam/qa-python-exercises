import pytest
from programs import list_of_squares

def test_list_of_squares():
    assert len(list_of_squares.list_of_squares(3)) == 3
   