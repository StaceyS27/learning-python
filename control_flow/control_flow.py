# Relational Operators: Equals and Not Equals

# comparators
    # equals: ==
    # not equals: !=

# True and False - first letter capitalized 
statement_one = True
statement_two = False 

#____________________________________________________________________________
# Boolean Variables 

# True and False are its own data type - bool

my_baby_bool = "true"
print(type(my_baby_bool))   
# prints <class 'str'>

my_baby_bool_two = True
print(type(my_baby_bool_two))
# prints <class 'bool'>

# boolean variables can be greated by ..
# 1. setting variable to true or false  or 
set_to_true = True
set_to_false = False

# 2. set a variable to equal a boolean expression 
bool_three = 3 * 3 == 9
print(bool_three)  # bool_three variable will now be True and will print that

#_______________________________________________________________________________
# If Statement 

# boolean variables and expressions are used to created conditional statements 
# if statement created using colon 

# boolean variable 
is_raining = True
if is_raining: 
    print("bring an umbrella")

# boolean expression
if 2 == 4-2:                # evaluates to true as well 
    print("apple")

#________________________________________________________________________________
# Relational Operators II

# boolean expressions are created with different relational operatiors 
    # >, >=, <, <=, !=, ==

credits = 120

if credits >= 120:
  print("You have enough credits to graduate")

#________________________________________________________________________________
# Boolean Operators: and

# boolean operators (also known as logical operators) 
# combines smaller boolean expressions into larger ones 
    # other examples are 'or' and 'not'

credits = 120
gpa = 3.4

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!") 
  
# will print statement bc both boolean expressions evaluate to true
# can also write each expression without parathesis 

# storing larger boolean expression within variable 
statement_one = (2+2+2 >= 6) and (-1*-1 < 0)

#__________________________________________________________________________________
# Boolean Operators: or

credits = 118
gpa = 2.0

if (credits>=120) or (gpa>=2):
  print("You have met at least one of the requirements.")

#___________________________________________________________________________________
# Boolean Operators: not

# reverses value of the variable/expression
not True == False
not False == True

not 1 + 1 == 2  # False
not 7 < 0       # True

# create checks using 'and' and 'not'
credits = 120                                 # will only print your gpa is not high enough to graduate 
gpa = 1.8

if not credits >= 120:
  print ("You do not have enough credits to graduate.")

if not gpa >= 2.0:                                              # will reverse expression value which is initially false to true
  print ("Your GPA is not high enough to graduate.")

if (not credits >= 120) and (not gpa >= 2.0):
  print ("You do not meet either requirement to graduate!")

#________________________________________________________________________________________
# Else Statements 

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):                         # both expressions have to evaluate to true so that the if statement can execute bc use of 'and'
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")    # will print this since gpa is too low 

#_________________________________________________________________________________________
# Else if Statements 

# in the if/else if/else block, if one of the if's are fullfilled, then exits block all together
# else if written as elif in python

grade = 86

if grade >= 90:               # will print "B" and since condition already met, will exist if/elif/else block entirely 
  print("A")                  # and not check the rest 
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else: 
  print("F")

