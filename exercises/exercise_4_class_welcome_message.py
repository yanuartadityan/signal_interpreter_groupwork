# exercise_4_class_welcome_message.py
class MyClass:
    def get_name_from_user(self):
        name = input("Enter your name: ")
        return name

def get_welcome_message():
    obj_class = MyClass();
    name = obj_class.get_name_from_user()
    welcome_message = f"Welcome {name}!"
    return welcome_message