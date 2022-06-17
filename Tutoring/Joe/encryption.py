
alpha = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "
]
# randomly generate beta alike:

    # available_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # letter_scramble = ""

    # for i in range(len(available_letters)):
    #     letter_index = randint(0, len(available_letters) - 1)
    #     chosen_letter = available_letters[letter_index]
    #     letter_scramble += chosen_letter
    #     available_letters = available_letters.replace(chosen_letter, "")

    # print(letter_scramble)

beta = [
    "j", "f", "y", "d", "h", "u", "r", "a", "g", "o", "b", "x", "e", "k", "m", " ", "v", "n", "q", "l", "s", "i", "c", "p", "t", "z", "w"
]
message_encrypted = ""
message_decrypted = ""


encrypt_or_decrypt = input("(E)ncrypt or (D)ecrypt: ").lower()

if encrypt_or_decrypt == "e":
    message_plaintext = input("Enter plaintext message: ")

    pos = 0
    for letter in message_plaintext:
        letter_index = alpha.index(letter)
        message_encrypted += beta[(letter_index + pos) % len(beta)]

        pos += 1

    print(message_encrypted)

# Still need to change to work with moving ceasar cipher as implimented on the encrypt
if encrypt_or_decrypt == "d":
    message_plaintext = input("Enter encrypted message: ")

    pos = 0
    for letter in message_plaintext:
        letter_index = (beta.index(letter) - pos) % len(beta)
        message_decrypted += alpha[letter_index]

        pos += 1

    print(message_decrypted)
