hang_image_progression = [
    """
    __________
    |/      |
    |
    |
____|____
 |     |
    """,
    """
    __________
    |/      |
    |       O
    |
____|____
 |     |
    """,
    """
    __________
    |/      |
    |       O
    |       |
____|____
 |     |
    """,
    """
    __________
    |/      |
    |       O
    |      /|
____|____
 |     |
    """,
    """
    __________
    |/      |
    |       O
    |      /|\\
____|____
 |     |
    """,
    """
    __________
    |/      |
    |       O
    |      /|\\
____|____  /-
 |     |
    """,
    """
    __________
    |/      |
    |       O
    |      /|\\
____|____  /-\\
 |     |
    """
]

secret_word = "fire pit"
guessed_letters = []

user_guess_max = 6
user_guess_count = 0




def CollectUserGuess():
    user_letter = input("\nEnter Letter Choice: ").replace(" ", "").lower()

    while IsUserGuessValid(user_letter) == False:
        user_letter = input("Enter Letter Choice: ").replace(" ", "").lower()
    
    guessed_letters.append(user_letter)
    return user_letter



def IsUserGuessValid(user_letter):
    if len(user_letter) != 1:
        print("\nPlease guess a single letter.")
        return False

    elif user_letter in guessed_letters:
        print("\nThat letter has already been guessed.")
        return False
    
    else:
        return True



while user_guess_count < user_guess_max:
    user_guess = CollectUserGuess()

    if user_guess in secret_word:
        print("hit")
    else:
        user_guess_count += 1

    print("\n\n\n" + hang_image_progression[user_guess_count])
    print("_ _ _ _ _")
    print("Remaining Guesses:", user_guess_max - user_guess_count)
    print("Guessed Letters:", str(guessed_letters).replace("\'", "").upper())