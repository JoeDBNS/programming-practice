

# Dynamic Random Group Maker
# -----------------------------------------
# Build randomly generated groups of students from a defined student list and
# group size.


# Requirements
# -------------
#     - Collect list of students
#     - Have default list of students for testing purposes
#     - Collect desired group size
#     - Randomly assign students to groups
#     - Return built groups list and any students left out



from copy import copy
from math import floor
from random import choice


def BuildRandomGroups(student_list, group_size):
    working_student_list = copy(student_list)

    group_count = floor(len(working_student_list) / group_size)

    random_groups = []
    for x in range(group_count):
        random_groups.append([])

    for group in random_groups:
        for x in range(group_size):
            chosen_student = choice(working_student_list)
            group.append(chosen_student)
            working_student_list.remove(chosen_student)

    if len(working_student_list) > 0:
        random_groups.append(working_student_list)

    return random_groups



# length = 23
student_list = ['Joe', 'Beth', 'Jake', 'Josh', 'Tyler', 'Ethan', 'James', 'Adam', 'Bruce', 'Franny', 'Stuart', 'Kevin', 'Brian', 'Bob', 'Kathy', 'Sarah', 'Bertha', 'Marge', 'Tom', 'Jess', 'Mike', 'Jay', 'Rich']

for group in BuildRandomGroups(student_list, 4):
    print(group)

print()

for group in BuildRandomGroups(student_list, 3):
    print(group)

print()

for group in BuildRandomGroups(student_list[0:8], 2):
    print(group)

print()

for group in BuildRandomGroups(student_list[0:16], 3):
    print(group)