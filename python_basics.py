# -------------------- Python Basic Commands --------------------------

# 1) How to print on console
print("Hello world!")

# 2) Variables
integer_number = 1
float_number = 1.5
name = "Andres"
last_name = "Lopez"
flag = True

# 3) Arithmetic Operators
addition = 2 + 3
substract = 3 - 1
multiplication = 5 * 3
float_division = 15 / 4
integer_division = 15 // 4
exponent = 5 ** 5

# 4) commands for string
final_string = "The student is " + name
final_string = "The student is %s" % name
final_string = "The Student is {}".format(name)
final_string = "Welcome back {b} {a}".format(a=name, b=last_name)
final_string = final_string.lower()
final_string = final_string.upper()
final_string = final_string.split(' ')

# 5) Strings as Lists
final_string[0]
final_string[0:10]
final_string[0:10:2]
final_string[::-1]  # reverse string

# 6) Lists
my_list = ["strings", 1.5, 3, False]
my_list.append("second name")
my_list.insert(2, "insert")
my_list.remove(3)
last_value = my_list.pop()
my_list.sort()

# 7) Tuples   - Inmutables
my_tuple = (1, "String", True)
my_tuple[0:2]

# 8) Dictionaries
first_dictionary = {'name': 'Gaudy', 'last_name': 'Lopez'}
second_dictionary = {'age': 20, 'student': False}

second_dictionary['teacher']: True

name = first_dictionary['name']
name = first_dictionary.get('name', 'key not found')

del second_dictionary['student']

first_dictionary.update()

keys = list(first_dictionary.keys())
values = tuple(first_dictionary.values())

# 9) Conditionals
if True:  # ==    >     <     >=     <=     !=
    print('it is true')
elif False:  # [] () {} 0 None  those ones can be used as false
    print('it is false')
else:  # and   or
    print('What is it?')

#  _______For _____________________
