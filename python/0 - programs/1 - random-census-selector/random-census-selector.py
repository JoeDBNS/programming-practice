import random


file_name = input('What Is The File Name?\t\t\t')

file_row_count = int(input('How Many Lines Does That File Contain?\t'))

record_count = input('How Many Random Records Do You Want?\t')

print('\n\n')

record_count_as_int = int(record_count)

random_number_set = []

records_to_return = []


while len(random_number_set) != record_count_as_int:
    new_random_number = random.randint(1, file_row_count)
    if (new_random_number not in random_number_set):
        random_number_set.append(new_random_number)


read_file_position = 1
with open(file_name + '.csv') as infile:
    for line in infile:
        if (read_file_position in random_number_set):
            records_to_return.append(line)
        read_file_position += 1


new_file = open('mock_random_set_of_' + record_count + '.csv','w+')
for record in records_to_return:
    new_file.write(record)
new_file.close()