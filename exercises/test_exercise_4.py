# test_exercise_4.py
import types
from unittest import TestCase
from unittest.mock import patch
from exercise_4_class_welcome_message import MyClass, get_welcome_message
from exercise import RandomClass, play_game_class

@patch.object(MyClass, 'get_name_from_user')
def test_get_welcome_message_with_decorator(mock_get_name_from_user):
    mock_get_name_from_user.return_value = "John"
    assert get_welcome_message() == "Welcome John!"

def test_get_welcome_message_with_context_manager():
    with patch.object(MyClass, 'get_name_from_user', return_value="John"):
        assert get_welcome_message() == "Welcome John!"

# exercise 4 -- mock get_robot_choice in play_game
@patch.object(RandomClass, 'get_robot_choice')
def test_get_robot_choice_class(mock_get_robot_choice):
    mock_get_robot_choice.return_value = "scissor"
    rc = RandomClass()
    assert rc.get_robot_choice() == "scissor"

@patch('builtins.input')
def test_play_game_class_1(mock_input):
    mock_input.return_value = "rock"
    with patch.object(RandomClass, 'get_robot_choice') as mock_random_class:
        play_game_class()
        mock_random_class.assert_called_once()

@patch('builtins.input')
# @patch.object(RandomClass, 'get_robot_choice')
def test_play_game_class_2(mock_input):
    mock_input.return_value = "rock"
    with patch.object(RandomClass, 'get_robot_choice') as mock_get_robot_choice:
        mock_get_robot_choice.return_value = "paper"
        assert play_game_class() == "You lost."
