""" confsource.py """


def find_fruits(input_list):
    """ find_fruits """
    fruit_list = ["banana", "apple", "orange"]
    all_found_fruits = [x for x in input_list if x in fruit_list]
    return all_found_fruits

def find_veggies(input_list):
    """ find veggies """
    veggie_list = ["broccoli", "carrot"]
    all_found_veggies = [x for x in input_list if x in veggie_list]
    return all_found_veggies
