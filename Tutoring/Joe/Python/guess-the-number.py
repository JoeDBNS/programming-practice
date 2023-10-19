# 'Guess the Number' Game
# -----------------------------------------
# Computer picks a random number and you have three guesses to guess the number.


# Requirements
# -------------
#     - If you guess high the computer needs to tell you. Same for a low guess.



from random import randint


goal_number = randint(1, 25)
remaining_guesses = 3

player_won = False

while remaining_guesses > 0:
    print('\nRemaining Guesses:', remaining_guesses)
    player_guess = int(input('Enter your guess: '))

    if player_guess > goal_number:
        print('\nYour guess was too high.')
    elif player_guess < goal_number:
        print('\nYour guess was too low.')
    else:
        player_won = True
        remaining_guesses = 0

    remaining_guesses -= 1

if player_won == False:
    print('\nYou have lost. Better luck next time.')
else:
    print('\nCorrect! You Win!')