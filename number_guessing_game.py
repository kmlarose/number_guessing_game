import random

def guess_a_number(lowest_possible_number, highest_possible_number, guesses):
    while True:
        guess = random.randint(lowest_possible_number, highest_possible_number)
        if guess in guesses:
            continue
        else:
            guesses.append(guess)
            break
    return guess


def new_game():
    print("""Please think of a number between 1 and 10, and I'll try to guess it in 5 tries.""")
    input("Press Enter when you've got it ")
    print("""Great! Here we go then... 
""")

    won_game = False
    guesses = []
    lowest_possible_number = 1
    highest_possible_number = 10

    # while i still have guesses...
    while len(guesses) < 5:

        # if there's only one possible option left...
        if highest_possible_number == lowest_possible_number:
            guess = lowest_possible_number
            print("Then it's gotta be {}!".format(guess))
            won_game = True
            break
        # otherwise, guess a number
        else:
            guess = guess_a_number(lowest_possible_number, highest_possible_number, guesses)

        # ask the user if game guessed right
        user_feedback = input("""
Was {} your number? y/N """.format(guess))
        if user_feedback.lower() == 'y':
            print("Yehaw! I gotcha!")
            won_game = True
            break
        else:
            if guess == highest_possible_number:
                highest_possible_number -= 1
            elif guess == lowest_possible_number:
                lowest_possible_number += 1
            else:
                print("""
Drat! Is your number higher or lower than {}?""".format(guess))
                clue = input("Enter 'H' for higher, or 'L' for lower ")
                if clue.lower() == 'h':
                    lowest_possible_number = guess + 1
                elif clue.lower() == 'l':
                    highest_possible_number = guess - 1
                else:
                    print("Don't wanna help me, eh? Fine then...")

    if not won_game:
        print("""
game over man! I have failed...""")

    if input("""
Wanna play again? Y/n """).lower() != 'n':
        new_game()


new_game()