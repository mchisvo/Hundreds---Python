
"""  Michael Lampard Chisvo mlampa01 ID No. 13132791
    This program is simple version of the game hundreds. The program allows the user to decide whether or
    not to roll the die dependant on input."""


import random


def instructions():
    """Function to tell the user the rules"""

    rules = """\n\tWelcome to Hundreds! Its you against the computer, the first one to 100 wins.
    Each turn the player rolls a 6 sided die as many times as they like. Be careful though,
    if you roll a 1 you lose all points for that turn, so decide whether or not to play it safe
    or go for glory. If the computer reaches a 100 you will have one extra turn to beat its score\n"""
    print(rules)
    breaker()


def game_status(computer_score, human_score):
    """Function to update the user on games scores and the difference between them."""

    print("Computers Score =  " + str(computer_score) + "\n")
    print("Human Score =  " + str(human_score) + "\n")
    difference = human_score - computer_score
    if difference < 0:
        print("The computer is winning by " + str(abs(difference)) + "\n")
    else:
        print("You are winning by " + str(abs(difference)) + "\n")
    breaker()


def breaker():
    """ Function to print === signs after each step, making the output look tidier."""

    console_break = "====="
    print(console_break * 10)


def ask_yes_or_no(prompt):
    """Prints the prompt as a question to the user."""

    roll_again = ('y', 'Y')
    stop_turn = ('n', 'N')
    while True:
        if prompt in roll_again:
            return True
        elif prompt in stop_turn:
            return False
        else:
            prompt = input("Would you like to roll?: ")
            continue


def human_move(computer_score, human_score):
    """Updates the user on score using game_status and then repeatedly asks if the user
    wants to roll again. The function then returns the total for the humans move."""

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
    return human_score


def computer_risk(computer_score, human_score):
    """A function to decide how risky the computer should play. If the computer is trailing
    by too much it will begin to roll the dice more times."""

    difference = computer_score - human_score
    if difference < 0 and abs(difference) > 20:
        roll_limit = random.randint(4, 8)
    else:
        roll_limit = random.randint(1, 4)
    return roll_limit


def computer_move(computer_score,human_score):
    """The computer rolls some number of times, displays the result of each roll, and the
    function returns the result. Uses computer_risk to decide how many times to roll."""

    move_total = 0
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
    """A function to generate the random number when a dice is rolled."""

    roll = random.randint(1, 6)
    return roll


def is_game_over(computer_score, human_score):
    """Returns True if either player has 100 or more, and the players are
    not tied, otherwise it returns False."""

    if human_score >= 100 or computer_score >= 100 and computer_score != human_score:
        return True
    else:
        return False


def show_results(computer_score, human_score):
    """Shows the final result of the game and identifies the winner."""
    print("**************************" + "\n")
    print("The Computer scored: " + str(computer_score) + "\n")
    print("You scored: " + str(human_score) + "\n")
    if computer_score > human_score:
        print("YOU LOST :( !")
    else:
        print("YOU WON :) !")

def main():
    """The main function executes the game and displays the winner at the end."""

    computer_score = 0
    human_score = 0
    finished = False
    instructions()
    while not finished:
        computer_score = computer_move(computer_score, human_score)
        if computer_score >= 100:
            human_score = human_move(computer_score, human_score)
            finished = True
        else:
            human_score = human_move(computer_score, human_score)
            finished = is_game_over(computer_score, human_score)

    show_results(computer_score, human_score)


main()