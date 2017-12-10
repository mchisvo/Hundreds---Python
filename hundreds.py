import random


def roll():
    """A function to generate the random number when a dice is rolled"""

    roll = random.randint(1, 6)
    return roll



def human_move(computer_score, human_score):
    #turn variables
    turn_total = 0 # Initialize turn total variable for function
    finished = False
    # Constants
    roll_again = ('y', 'Y')

    while not finished:



        print("Computers Score =  " + str(computer_score) + "\n")
        print("Human Score =  " + str(human_score))
        difference = human_score - computer_score
        print("The scores difference is " + str(difference))

        print("Would you like to roll?", end='' )
        user_choice = input()
        if user_choice in roll_again:

            roll_number = roll()
            turn_total = turn_total + roll_number
            print(roll_number, turn_total)
        else:
            finished = True

def main():
    # Global variables
    computer_score = 0
    human_score = 0

    human_move(computer_score, human_score)

main()