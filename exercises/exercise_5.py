# exercise_5
def increment_by_10(number):
    number += 10
    return number

def print_fun_fact():
    age = input("enter your age: ")
    new_age = increment_by_10(int(age))
    print(f"In 10 years you will be {new_age} years old.")