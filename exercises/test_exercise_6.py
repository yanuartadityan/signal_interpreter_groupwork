from unittest.mock import patch, call
from exercise_6 import print_greetings
from exercise import get_robot_choice


@patch('builtins.print')
def test_print_greetings(mock_print):
    print_greetings()
    assert mock_print.mock_calls == [call("Hello World"), call("Goodbye")]

@patch('builtins.print')
def test_print_get_robot_choice(mock_print):
    with patch('exercise.random.choice', return_value="rock"):
        get_robot_choice()
        assert mock_print.mock_calls == [call("Robot will play: rock")]

