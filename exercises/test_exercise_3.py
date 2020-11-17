# test_exercise_3
from unittest.mock import patch
from exercise_3_get_welcome_message import get_welcome_message

# wrong way to patch a function, taken from the source file the function is declared
# @patch('exercise_3_get_name_from_user.get_name_from_user', return_value="Jimbo")
# def test_get_welcome_message(mock_get_name_from_user):
#     assert get_welcome_message() == f"Welcome to the stage {mock_get_name_from_user()}"

# correct way to patch a funciton, taken from the file where the function is 'called'
@patch('exercise_3_get_welcome_message.get_name_from_user', return_value="Jimbo")
def test_get_welcome_message_correct(mock_get_name_from_user):
    assert get_welcome_message() == f"Welcome to the stage {mock_get_name_from_user()}"