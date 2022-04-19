from ast import Pass


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


dog_1 = Dog('Fido')
dog_2 = Dog('Buddy')

dog_1.add_trick('roll over')
dog_2.add_trick('play dead')

dog_1.tricks
print(dog_1.tricks)
# ['roll over']
dog_2.tricks
print(dog_2.tricks)
# ['play dead']




print('\n\n')




class Employee:

    def __init__(self, name_first, name_last):
        self.name_first = name_first
        self.name_last = name_last
        self.name_full = self.name_first + " " + self.name_last

john = Employee('John', 'Doe')  # Create an empty employee record

# Fill the fields of the record
john.dept = 'computer lab'
john.salary = 1000

print(john)
print(john.name_full)
print(john.salary)




print('\n\n')




class Pet:
    Pass

Bobby = Pet()  # Create an empty Pet record

# Fill the fields of the record
Bobby.type = 'cat'
Bobby.name = 'Bobby'

print(Bobby.type)
print(Bobby.name)