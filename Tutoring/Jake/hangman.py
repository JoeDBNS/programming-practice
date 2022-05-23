# Make a random list of words that the computer will select from 
# Allow the user to guess letter by letter until the word is either
# completed or the man is fully hung.


import random


# number_of_failures = 0
# word_list = ["defend", "feces", "desire", "test", "frazzled", "participate", "indecisive", "there", "until", "pasta", "tendon"]
# computer_word_choice = random.choice(word_list)
# completed_word = ""
# correct_letters = ""
# hangman_complete = False


# while hangman_complete == False:

#     player_letter_choice = input("Guess a letter: ")


#     for letter in computer_word_choice:

#         if letter in correct_letters:
#             completed_word += letter

#         elif letter == player_letter_choice:
#             completed_word += player_letter_choice
#             if player_letter_choice not in correct_letters:
#                 correct_letters += player_letter_choice 
            
#         elif letter != player_letter_choice and letter not in correct_letters:
#             completed_word += "_"
    
#     if player_letter_choice not in computer_word_choice and letter not in correct_letters:
#             print("That letter is not in the word.")
    
#     print(completed_word)

#     if "_" not in completed_word:
#         print("You have figured out what word it is, congratulations!")
#         hangman_complete = True
    
    
#     completed_word = ""











number_of_failures = 0
word_list = ["defend", "feces", "desire", "test", "frazzled", "participate", "indecisive", "there", "until", "pasta", "tendon"]
secret_word = random.choice(word_list)
secret_word_display = ""
correct_letters = []
hangman_complete = False


def BuildSecretWordDisplay():
    secret_word_building = ""

    for letter in secret_word:
        if letter in correct_letters:
            secret_word_building += letter

        elif letter == user_guess:
            secret_word_building += user_guess

            if user_guess not in correct_letters:
                correct_letters.append(user_guess)

        elif letter != user_guess and letter not in correct_letters:
            secret_word_building += "_"

    return secret_word_building


while hangman_complete == False:
    user_guess = input("\nGuess a letter: ")

    secret_word_display = BuildSecretWordDisplay()
    
    if user_guess not in secret_word:
            print("That letter is not in the word.")
            number_of_failures += 1
    
    print(secret_word, "-", secret_word_display, "-", correct_letters)

    if "_" not in secret_word_display or number_of_failures > 5:
        hangman_complete = True


if "_" not in secret_word_display:
    print("\n\nYou have figured out what word it is, congratulations!")
else :
    print("\n\nBetter luck next time!")