import random
from unittest.mock import patch
from exercise import check_input, decide_who_will_win, get_robot_choice, play_game

############
# exercise 1
############
def test_check_input():
    assert check_input("rock") == True
    assert check_input("scissor") == True
    assert check_input("paper") == True
    assert check_input("13paper") == False
    assert check_input("pape") == False

def test_who_will_win():
    assert decide_who_will_win("rock", "scissor") == "You won!"
    assert decide_who_will_win("rock", "paper") == "You lost."
    assert decide_who_will_win("rock", "rock") == "It was a tie"
    assert decide_who_will_win("scissor", "rock") == "You lost."
    assert decide_who_will_win("scissor", "paper") == "You won!"
    assert decide_who_will_win("scissor", "scissor") == "It was a tie"
    assert decide_who_will_win("paper", "rock") == "You won!"
    assert decide_who_will_win("paper", "scissor") == "You lost."
    assert decide_who_will_win("paper", "paper") == "It was a tie"

############
# exercise 2
############
# 2a
def test_check_input_mock():
    with patch('exercise.check_input', return_value=False) as mock_input:
        assert check_input(mock_input) == mock_input()

def test_get_robot_choice():
    with patch('exercise.random.choice', return_value="rock") as mock_input:
        assert get_robot_choice() == mock_input()

# 2b
def test_play_game_rbt_choice():
    with patch('exercise.random.choice', return_value="rock") as mock_input:
        assert get_robot_choice() == mock_input()

@patch('builtins.input')
# @patch('exercise.get_robot_choice')
def test_play_game(mock_input):
    with patch('exercise.get_robot_choice', return_value="paper") as mock_get_robot_choice:
        mock_input.return_value = "rock"
    # mock_get_robot_choice.return_value = "scissor"
        assert play_game() == "You lost."
