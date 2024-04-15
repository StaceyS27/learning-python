# comments are written this way 

# Print
print("hello world")  # what is used instead of console.log()


# Strings - can use single and double quotes like javascript 
print('hello world')


# Variables 
    # can't have spaces or symbols other than underscore ( _ )
    # can't start w/ numbers but can have them after first letter 

message = "hasta la vista"
print(message)

#_______________________________________________________________________________________
# Errors
    # two common types of errors occur while writing python: SyntaxError and NameError
    # 1. SyntaxError - something is wrong with usage of language 
        # use of punctuation, paranthesis, command etc
    # 2. NameError - occurs when python interpreter does not recognize a word 
        # a variable that is never defined will throw this error 

#_______________________________________________________________________________________
# Numbers
    # python has a few numberic data types 
        # 1. integer - (int) is a whole number ex: 1,2,3 also -1,-2,-2 and 0
        # 2. floating-point number - (float) is a decimal

# Define the release and runtime integer variables below:
release_year = 1
runtime = 10

# Define the rating_out_of_10 float variable below: 
rating_out_of_10 = 2.5
print(rating_out_of_10)

#_______________________________________________________________________________________________
# Calculations
    # python performs arithmetic operations (addition, subtraction multiplication, division)
    # when dividing integers though, all ints are converted to floats before performing divison
        # in earlier python when this didn't happen, integer division would round down to nearest integer 
        # now: print(10/5) would result in 2.0

#__________________________________________________________________________________________________
# Exponents 
    
# not easy to write exponents w/ keyboards so use this notation **
print(2 ** 10) # means 2 to the 10th power or 1024
print(8 ** 2) # 64

#____________________________________________________________________________________________________
# modulo

# as the divdend increases by 1, so does the remainder
# until we reach a number that is evenly divisible by the divisor (remainder now 0)
# ex: 4%3=1, 5%3=2, 6%3=0

# modulo operator useful when want to perform something on the nth time something occurs
# ex: 7th customer gets a servey so everytime a customer(who is numbered)%7=0, receive a servey 
    # 7th, 14th, 21st, etc 

order_263_r = 263 % 11              # every 11th customer gets coupon but bc modulo results in 10, no coupon 
print(order_263_r)
order_263_coupon = "no"

order_264_r = 264%11
print(order_264_r)                  # results in 0
order_264_coupon = "yes"

#_______________________________________________________________________________________________________
# Concatenation

# '+' operator used to add two strings together - string concatenation 
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text

# Prints "Hey there!How are you doing?"             # need to add empty string to create space b/w text
print(full_text)

full_text = "greeting_text" + " " + question_text
print(full_text)                                    # now: Hey there! How are you doing?"


# to concatenate a string with a number, need to convert the number to a string first
# use the str() function 
birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"

full_birthday_string = birthday_string + str(age) + birthday_string_2
print(full_birthday_string)

# can also just pass a string and a number into print() as seperate arguments as well
# without having to convert the number into a string 
print(birthday_string, age, birthday_string_2)              # still prints "I am  10  years old today!" (but w/ extra spaces)

#_________________________________________________________________________________________________________
# Plus Equals


