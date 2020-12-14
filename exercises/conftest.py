""" conftest.py """
import pytest
from confsource import find_fruits, find_veggies


@pytest.fixture
def fruits_and_veggies():
    """ fruits_and_veggies"""
    return ["apple", "banana", "broccoli", "carrot", "orange"]

def test_find_fruits(fruits_and_veggies):
    """ test_find_fruits """
    assert find_fruits(fruits_and_veggies) == ["apple", "banana", "orange"]

def test_find_veggies(fruits_and_veggies):
    """ test_find_veggies """
    assert find_veggies(fruits_and_veggies) == ["broccoli", "carrot"]
