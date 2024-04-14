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



