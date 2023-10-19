import random


test_sentence = "This is a test string."

double_test_sentence = test_sentence + " " + test_sentence

test_sentence[8]

test_sentence[-1]

double_test_sentence = double_test_sentence.replace("string", "double string")




big_number = (7 * (2 + 3))

big_number += 5

final_answer = "The number __ is the correct number"

final_answer = final_answer.replace("__", str(big_number))




big_number = (7 * (2 + 3))

big_number %= 3

final_answer = "The number " + str(big_number) + " is the correct number"




many_names_string = "Kenny Lenny Bobbie Bobby Tina Dina Joe Schmoe"

lower_split = many_names_string.lower()

split_text = lower_split.split()






random_number = random.randint(0, 100)

more_than = " is greater than 50"

less_than = " is less than 50"


# if random_number < 50:
#     print(str(random_number) + less_than)
# elif random_number > 50:
#     print(str(random_number) + more_than)
# else:
    # print("Number is", 50)






random_number = random.randint(1, 400)

# 1-100
zero_hun_list = []
# 101-200
one_hun_list = []
# 201-300
two_hun_list = []
# 301-400
three_hun_list = []

if random_number <= 100:
   zero_hun_list.append(random_number)
elif random_number >= 101 and random_number <= 200:
    one_hun_list.append(random_number)
elif random_number >= 201 and random_number <= 300:
    two_hun_list.append(random_number)
elif random_number >= 301 and random_number <= 400:
    three_hun_list.append(random_number)

print("1-100:\t\t", zero_hun_list)
print("101-200:\t", one_hun_list)
print("201-300:\t", two_hun_list)
print("301-400:\t", three_hun_list)
















student_1 = "Stuart"

# Print student_1

# Find what character the name starts with

# If name starts with "S", then print "true", otherwise print "false"

student_2 = "stuart"

# Print student_2

# Find what character the name starts with

# If name starts with "S", then print "true", otherwise print "false"

student_3 = "Tyler"

# Print student_3

# Find what character the name starts with

# If name starts with "S", then print "true", otherwise print "false"




student_list = ["joe", "Beth", "Jake", "josh", "tyler", "Ethan", "james", "Adam", "Bruce", "franny", "Stuart", "Kevin", "brian", "bob", "kathy", "Sarah", "bertha", "Marge", "tom", "Jess", "Mike", "Jay", "rich"]

# Print 10th index of student_list

# Find what character the name starts with

# If name starts with "S", then print "true", otherwise print "false"




# Build loop that prints each name from student_list

# Build same thing but using the other kind of loop (while/for)




# Build loop that iterates through student_list

# Find what character each name starts with

# If name starts with "S", then print "true", otherwise print "false"


# Build same thing but using the other kind of loop (while/for)




