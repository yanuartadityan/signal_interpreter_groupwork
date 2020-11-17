# exercise_3_get_welcome_message.py

from exercise_3_get_name_from_user import get_name_from_user

def get_welcome_message():
    name = get_name_from_user()
    welcome_message = f"Welcome to the stage {name}"
    return welcome_message

