import random


def game_status(computer_score, human_score):
    """Function to print game status"""
    print("Computers Score =  " + str(computer_score) + "\n")
    print("Human Score =  " + str(human_score))
    difference = human_score - computer_score
    print("The scores difference is " + str(difference)+ "\n")
    breaker()


def breaker():
    """ Function to print === signs after each step, making the output look tidier"""
    breaker = "====="
    print(breaker * 10)


def ask_yes_or_no(prompt):
    roll_again = ('y', 'Y')
    stop_turn = ('n', 'N')

    if prompt in roll_again:
        return True
    elif prompt in stop_turn:
        return False
    else:
        print("wrong")



def human_move(computer_score, human_score):
    game_status(computer_score, human_score)

    if ask_yes_or_no(prompt = input("Would you like to roll?:")):
        print(roll())

def roll():
    """A function to generate the random number when a dice is rolled"""

    roll = random.randint(1, 6)
    return roll

def main():
    # main function variables
    computer_score = 0
    human_score = 0

    #computer_score = computer_move(computer_score, human_score)

    human_score = human_move(computer_score, human_score)

    print(computer_score, human_score) # How do you bring the function variables out



main()