""" test_exercise_w4_2.py """
import pytest
from unittest.mock import patch, call
from exercise_w4_2 import bus_validator


@pytest.mark.parametrize("age, expected_value", [
    ("OK", "You have entered an invalid input"),
    ("24", "Congratulations, you are old enough to drive a bus"),
    ("30", "Congratulations, you are old enough to drive a bus"),
    ("21", "Sorry, you have to wait 3 more years to drive a bus"),
    ("3f", "You have entered an invalid input")])
def test_bus_validator(age, expected_value):
    """ test_bus_validator """
    with patch("builtins.print") as mock_print:
        with patch("builtins.input") as mock_input:
            mock_input.return_value = age
            bus_validator()
            assert mock_print.mock_calls == [call(expected_value), call("Good bye!")]
