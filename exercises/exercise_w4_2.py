""" exercise_w4_2.py """

def bus_validator():
    """ bus_validator """
    try:
        user_age = int(input("Enter your age: "))
    except ValueError:
        print("You have entered an invalid input")
    else:
        if user_age >= 24:
            print("Congratulations, you are old enough to drive a bus")
        else:
            print(f"Sorry, you have to wait {24-user_age} more years to drive a bus")
    finally:
        print("Good bye!")
