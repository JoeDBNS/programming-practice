import random


# txt = "Hello, welcome to my world. welcome"

# search_find = txt.find("wel", 10, 35)
# search_index = txt.index("wel")

# print(search_find)
# print(search_index)




string_list = ['this', 'is', 'An', 'array', 'Of', 'is', 'an', 'strings', 'stinky']


starting_string = 'this is A string Of stinky'
practice_string = starting_string.lower()[3:7]


# # print(string_list[14])

# print(string_list.index('array'))

# print('is' in string_list)

# print(len(string_list))




# for item in string_list:
#     if item.lower() == 'an':
#         string_list.remove(item)

# print(string_list)



# person_list = [
#     {
#         "first_name": "Joe",
#         "last_name": "Davis"
#     },
#     {
#         "first_name": "Jake",
#         "last_name": "Davis"
#     },
#     {
#         "first_name": "Josh",
#         "last_name": "Friel"
#     }
# ]



# jake_person_list = [
#     {
#         "first_name": "Jake",
#         "last_name": "Davis"
#     }
# ]

# print(person_list[1]["first_name"])






available_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_scramble = ""

for i in range(len(available_letters)):
    letter_index = random.randint(0, len(available_letters) - 1)
    chosen_letter = available_letters[letter_index]
    letter_scramble += chosen_letter
    available_letters = available_letters.replace(chosen_letter, "")

print(letter_scramble)




saturn = "Joey wears clown shoes!"
newstring = ""

for char in saturn:
    newstring += char + char

print(newstring)