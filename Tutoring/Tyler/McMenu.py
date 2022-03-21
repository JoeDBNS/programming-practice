operator = ""
num_one_text = ""
num_two_text = ""
num_one_int = 0
num_two_int = 0
num_list = []
operator_list = []
master_number = 0
continue_numbers = ""


num_one_text = input("Enter starting number:\n")
num_one_check_pass = False
while num_one_check_pass != True:
    try:
        num_one_int = float(num_one_text)
        num_one_check_pass = True
    except:
        num_one_text = input("\nInvalid starting number please enter valid number:\n")
        num_one_check_pass = False
num_list.append(num_one_int)

operator = input("\nEnter operator:\n")
while operator != "-" and operator != "+":
    operator = input("\nInvalid operator please enter valid operator:\n")
operator_list.append(operator)

num_two_text = input("\nEnter secondary number:\n")
num_two_int = float(num_two_text)
num_list.append(num_two_int)

continue_numbers = input("\nWould you like to continue? (y/n):\n")

while continue_numbers == "y":
    operator = input("\nEnter operator:\n")
    while operator != "-" and operator != "+":
        operator = input("\nInvalid operator please enter valid operator:\n")
    operator_list.append(operator)

    num_two_text = input("\nEnter secondary number:\n")
    num_two_int = float(num_two_text)
    num_list.append(num_two_int)

    continue_numbers = input("\nWould you like to continue? (y/n):\n")
    

master_number += num_list[0]


i = 0
for x in operator_list:
    if x == "+":
        master_number += num_list[i + 1]
    if x == "-":
        master_number -= num_list[i + 1]

    i += 1

print("\nMaster number:", master_number)