""" test_exercise_w4_1.py """
import pytest
from exercise_w4_1 import convert_to_comma_separated_string, convert_to_space_separated_string


@pytest.fixture
def some_numbers_list():
    """ some_numbers_list """
    return ["one", "two", "three"]

def test_comma_separated(some_numbers_list):
    """ test_comma_separated """
    assert convert_to_comma_separated_string(some_numbers_list) == \
        "one,two,three"

def test_space_separated(some_numbers_list):
    """ test_space_separated """
    assert convert_to_space_separated_string(some_numbers_list) == \
        "one two three"

