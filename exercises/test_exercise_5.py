# test_exercise_5.py
from unittest.mock import patch
from exercise_5 import print_fun_fact
from exercise import play_game


@patch('exercise_5.increment_by_10')
@patch('builtins.input')
def test_print_fun_fact(mock_input, mock_increment_by_10):
    mock_input.return_value = 5
    print_fun_fact()
    mock_increment_by_10.assert_called_with(5)


@patch('exercise.decide_who_will_win')
@patch('exercise.get_robot_choice')
@patch('builtins.input')
def test_play_game_correct_argument(mock_input, mock_get_robot_choice, mock_decide_who_will_win):
    mock_input.return_value = "rock"
    mock_get_robot_choice.return_value = "scissor"
    play_game()
    mock_decide_who_will_win.assert_called_with("rock", "scissor")
