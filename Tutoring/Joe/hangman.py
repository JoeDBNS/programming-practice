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

secret_word = ""
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



def BuildSecretWordDisplay():
    secret_word_display = secret_word

    for letter in secret_word_display:
        if letter != " ":
            if letter not in guessed_letters:
                secret_word_display = secret_word_display.replace(letter, "_")

    secret_word_display = " ".join(list(secret_word_display)).upper()

    return secret_word_display




secret_word = input("\nEnter the secret word: ").lower()

print("\n\n\n\n\n\n\n" + hang_image_progression[user_guess_count])
print(BuildSecretWordDisplay())
print("Remaining Guesses:", user_guess_max - user_guess_count)

while user_guess_count < user_guess_max:
    user_guess = CollectUserGuess()
    BuildSecretWordDisplay()

    if user_guess not in secret_word:
        user_guess_count += 1

    if BuildSecretWordDisplay().count("_") == 0:
        break

    print("\n\n\n" + hang_image_progression[user_guess_count])
    print(BuildSecretWordDisplay())
    print("Remaining Guesses:", user_guess_max - user_guess_count)
    print("Guessed Letters:", str(guessed_letters).replace("\'", "").upper())

if user_guess_count < user_guess_max:
    print("\n\n\nThe word was: " + BuildSecretWordDisplay())
    print("YOU'RE A WINNER!")
else:
    print("You've lost. Try again later.")