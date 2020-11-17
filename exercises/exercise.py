import random

############
# exercise 1
############
def check_input(input_choice):
    if input_choice in ["rock", "scissor", "paper"]:
        return True
    else:
        return False


def decide_who_will_win(fp_choice, sp_choice):
    print("deciding who will win...")
    if not (check_input(fp_choice) and check_input(sp_choice)):
        return "Wrong input\nMake sure inputs are either ['rock', 'scissor', 'paper']"

    if (fp_choice == "rock" and sp_choice == "scissor"):
        return "You won!"
    elif (fp_choice == "rock" and sp_choice == "paper"):
        return "You lost."
    elif (fp_choice == "scissor" and sp_choice == "paper"):
        return "You won!"
    elif (fp_choice == "scissor" and sp_choice == "rock"):
        return "You lost."
    elif (fp_choice == "paper" and sp_choice == "scissor"):
        return "You lost."
    elif (fp_choice == "paper" and sp_choice == "rock"):
        return "You won!"
    else:
        return "It was a tie"


############
# exercise 2
############
# 2a
def get_robot_choice():
    choice = random.choice(["rock", "paper", "scissor"])
    print(f"Robot will play: {choice}")
    return choice

# 2b
def play_game():
    player_input = input("what do you play: ")
    robot_answer = get_robot_choice()
    result = decide_who_will_win(player_input, robot_answer)
    return result


############
# exercise 4
############
class RandomClass:
    def get_robot_choice(self):
        choice = random.choice(["rock", "paper", "scissor"])
        print(f"Robot will play: {choice}")
        return choice

def play_game_class():
    rc = RandomClass()
    player_input = input("what do you play: ")
    robot_answer = rc.get_robot_choice()
    result = decide_who_will_win(player_input, robot_answer)
    return result


if __name__ == '__main__':
    print(play_game())