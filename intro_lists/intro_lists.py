# What is a List?

# a list is one of many built-in data structures that allow us to work with 
# a collection of data in sequential order (meaning contigous in memory)
heights = [61, 70, 67, 64, 65]

#________________________________________________________________________________
# What can a List contain?

# lists can contain, integers, strings and even multiple data types in one list 
# below it has a string, integer, boolean, and float datatype 
mixed_list_common = ["Mia", 27, False, 0.5]
sam_height_and_testscore = ["Sam", 67, 85.5, True]

#_________________________________________________________________________________
# Empty Lists
my_empty_list = []

#_________________________________________________________________________________
# List Methods

# append() adds element at the end of the list 
# will explore more methods 

example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)          # like push in js
# print(example_list)
print(example_list)             # [1, 2, 3, 4, 5]

#Using Remove
example_list.remove(5)          # like pop in js
# print(example_list)
print(example_list)             # [1, 2, 3, 4]

#_________________________________________________________________________________