import random


def game_status(computer_score, human_score):
    """Function to print game status"""
    breaker()
    print("Computers Score =  " + str(computer_score) + "\n")
    print("Human Score =  " + str(human_score) + "\n")
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
    finished = False
    move_total = 0
    game_status(computer_score, human_score)
    while not finished:
        if ask_yes_or_no(prompt = input("Would you like to roll?: ")):
            roll_number = roll()
            print('You rolled a: '+ str(roll_number))
            if roll_number == 1:
                move_total = 0
                print("You scored " + str(move_total) + " this move")
                breaker()
                finished = True
            else:
                move_total = move_total + roll_number

        else:
            print("You scored " + str(move_total) + " this move")
            breaker()
            finished = True
    human_score = human_score + move_total
    game_status(computer_score, human_score)
    return human_score


def computer_risk(computer_score, human_score):
    difference = computer_score - human_score
    if difference < 0 and abs(difference) > 20:
        print("yes")
        roll_limit = random.randint(4, 8)
    else:
        roll_limit = random.randint(1, 4)
    return roll_limit


def computer_move(computer_score,human_score):
    move_total = 0  # Initialize turn total variable for function
    roll_limit = computer_risk(computer_score, human_score)
    die_roll_count = 0
    finished = False
    while not finished:
        if die_roll_count != roll_limit:
            roll_number = roll()
            print("The computer rolled a: " + str(roll_number))
            if roll_number == 1:
                finished = True
                move_total = 0
            else:
                move_total = move_total + roll_number
                die_roll_count += 1
        else:
            print("Computer scored " + str(move_total) + " this move")
            breaker()
            finished = True

    computer_score = computer_score + move_total
    return computer_score

def roll():
    """A function to generate the random number when a dice is rolled"""

    roll = random.randint(1, 6)
    return roll


def is_game_over(computer_score, human_score):
    if human_score >= 50 or computer_score >= 50 and computer_score != human_score:
        return True
    else:
        return False




def main():
    # main function variables
    computer_score = 0
    human_score = 0
    finished = False
    while not finished:

        computer_score = computer_move(computer_score, human_score)
        if computer_score >= 50:
            human_score = human_move(computer_score, human_score)
            finished = True
        else:
            human_score = human_move(computer_score, human_score)
            finished = is_game_over(computer_score, human_score)


    print(computer_score, human_score)



main()