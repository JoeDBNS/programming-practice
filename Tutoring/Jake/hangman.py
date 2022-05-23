# Make a random list of words that the computer will select from 
# Allow the user to guess letter by letter until the word is either
# completed or the man is fully hung.


import random


number_of_failures = 0
word_list = ["defend", "feces", "desire", "test", "frazzled", "participate", "indecisive", "there", "until", "pasta", "tendon"]
computer_word_choice = random.choice(word_list)
completed_word = ""
correct_letters = ""
hangman_complete = False


while hangman_complete == False:

    player_letter_choice = input("Guess a letter: ")


    for letter in computer_word_choice:

        if letter in correct_letters:
            completed_word += letter

        elif letter == player_letter_choice:
            completed_word += player_letter_choice
            if player_letter_choice not in correct_letters:
                correct_letters += player_letter_choice 
            
        elif letter != player_letter_choice and letter not in correct_letters:
            completed_word += "_"
    
    if player_letter_choice not in computer_word_choice and letter not in correct_letters:
            print("That letter is not in the word.")
    
    print(completed_word)

    if "_" not in completed_word:
        print("You have figured out what word it is, congratulations!")
        hangman_complete = True
    
    
    completed_word = ""
