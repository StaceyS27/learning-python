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
# Growing a List: Append

# append is used to add a single element to the end of a list in python
orders = ["daisies", "periwinkle"]
print(orders)

orders.append("tulips")
orders.append("roses")

print(orders)   

#________________________________________________________________________________
# Growing a List: Plus (+)

# can use the + sign to combine two lists together 
    # known as concatenation
# cannot add integers with the list 
    # will get a type error stating that only lists, not int can be concatenated 

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]

# combine orders
orders_combined = orders + new_orders
print(orders_combined)

# only works when 4 is in the list, not an int itself 
broken_prices = [5, 3, 4, 5, 4] + [4]

#_________________________________________________________________________________
# Accessing List Elements
