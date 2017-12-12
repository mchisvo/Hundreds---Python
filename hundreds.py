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

        game_status(computer_score, human_score)

        print("Would you like to roll? ", end='' )
        user_choice = input()
        if user_choice in roll_again:

            roll_number = roll()

            turn_total = turn_total + roll_number
            print(roll_number, turn_total)
        else:
            finished = True
# Update human score - maybe just return human score and only print the turn total.
    return turn_total

def game_status(computer_score, human_score):
    """Function to print game status"""
    print("Computers Score =  " + str(computer_score) + "\n")
    print("Human Score =  " + str(human_score))
    difference = human_score - computer_score
    print("The scores difference is " + str(difference))



def computer_move(computer_score,human_score):

    turn_total = 0  # Initialize turn total variable for function
    # Ad risk logic. i.e compyer decides to only try 4 rolls instead of 10 when its ahead
    roll_limit = random.randint(1, 10)
    die_roll_count = 0 #
    finished = False

    while not finished:
        game_status(computer_score, human_score)
        if die_roll_count != roll_limit:
            roll_number = roll()
            turn_total = turn_total + roll_number
            print(roll_number, turn_total)
            if roll_number == 1:
                finished = True
                turn_total = 0
                print(roll_number, turn_total)
            else:
                turn_total = turn_total + roll_number
                die_roll_count += 1
        else:
            finished = True

    computer_score = computer_score + turn_total
    return computer_score



def main():
    # main function variables
    computer_score = 0
    human_score = 0

    computer_score = computer_move(computer_score, human_score)

    human_score = human_move(computer_score, human_score)

    print(computer_score, human_score) # How do you bring the function variables out
main()