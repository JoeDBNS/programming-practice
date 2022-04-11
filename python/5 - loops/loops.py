# For examples only,  not needed for loops
import string
import random






for x in [66, 10, 4]:
    print(x)



for y in ["First", "Second", "Third"]:
    print(y)



people = ["Jimbo", "Randy", "Clark", "Franny"]
for person in people:
    print(person)



for x in range(9):
    if (x < 5):
        print(x, "is less than 5")
    else:
        print(x, "is more than 5")



for x in range(0, 101, 10):
    print(x)



people_detailed = [
    {
        "name": "Jimbo",
        "age": 13
    },
    {
        "name": "Randy",
        "age": 42
    },
    {
        "name": "Clark",
        "age": 45
    },
    {
        "name": "Franny",
        "age": 69
    }
]
for person in people_detailed:
    age_plus_4 = person["age"] + 3
    print(person["name"] + " is", person["age"], "years old now and in three years they will be", age_plus_4, "years old.")



i = 1
while i < 4:
    print(i)
    i += 1


random.choice(string.ascii_letters)


randomly_built_string = ""
while len(randomly_built_string) < 100:
    randomly_built_string = randomly_built_string + random.choice(string.ascii_letters)
    print(randomly_built_string)