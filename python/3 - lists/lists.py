string_list = ['this', 'is', 'An', 'array', 'Of', 'strings']


number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


mixed_array = ['mixed', 3, 244, 'array']


combined_list = string_list + mixed_array


# list of dictionaries
[
    {
        'name': 'Timmy',
        'age': 11
    },
    {
        'name': 'Joe',
        'age': 25
    },
    {
        'name': 'Franny',
        'age': 18
    }
]


# list of lists
list_list = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]


string_list[1]


list_list[1][2]


string_list[::-1]


string_list[0::-1]


# Actually alters list
string_list.reverse()


len(string_list)


number_list.sort()


number_list.sort(reverse=True)


string_list.sort()


# The sort method has an optional key parameter. The parameter specifies a function to be called on each list element prior to making comparisons.
string_list.sort(key=str.lower)


string_list.index('An')


string_list.insert(4, 'stinky')


string_list.append('nonsense')
string_list.append('nonsense')


string_list.extend('nonsense')


string_list.pop()


# returns removed value
string_list.pop(4)


# does not return anything
del string_list[6]


string_list.remove('nonsense')


string_list.count('this')