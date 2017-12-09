import random

# Global variables
computer_score = 0
human_score = 0


def roll():
    """A function to generate the random number when a dice is rolled"""

    roll = random.randint(1, 6)
    return roll



#def human_move(computer_score, human_score):


while roll != 1:
    # Constants
    roll_again = ('y', 'Y')

    print("Computers Score =  " + str(computer_score) + "\n")
    print("Human Score =  " + str(human_score))
    difference = human_score - computer_score
    print("The scores difference is " + str(difference))

    print("Would you like to roll?", end='' + "\n")
    user_choice = input()


    print(roll())