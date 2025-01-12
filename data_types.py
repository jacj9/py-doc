# String data type

# literal assignment
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str('Pepperoni')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname+="!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?                                     

I was just checking in.   
                                    All good?

'''
print(multiline)

# Escaping special characters
sentence ='I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok")) # replace the word 'good' with the word 'ok'
print(multiline)

print(len(multiline)) # Count all the character in the string
multiline += "                                " # add whitespace
multiline = "                    " + multiline
print(len(multiline))

print(len(multiline.strip())) # remove all of the whitespace
print(len(multiline.lstrip())) # remove whitespace on the left side
print(len(multiline.rstrip())) # remove whitespace on the right side

print("")

# Build a menu
title = "menu".upper() # Set to all upper case
print(title.center(20, "=")) # title variable will be in the center. Fill out the space of 20 characters with "="
print("Coffee".ljust(16, ".") + "$1".rjust(4 )) # Left justify, placing sting "Coffee" to the left and '$1' to the right
print("Muffin".ljust(16, ".") + "$2".rjust(4 )) 
print("Cheesecake".ljust(16, ".") + "$4".rjust(4 ))

print("")

# string index values
print(first[1])
print(first[-1])
print(first[1:-1]) # end range does not retrieve the value
print(first[1:]) # leave end range empty to retrieve end value

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))


# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool)) # Check to see, is it a bool value?

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))         # type of integer
print(isinstance(best_price, int)) # check to see if it is it an integer?

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value)) # check the type for comp_value
print(comp_value.real)  # real number value
print(comp_value.imag) # imaginary number value

# Built-in functions for numbers

print(abs(gpa)) # absolute value
print(abs(gpa * -1))

print(round(gpa)) # round to the nearest integer

print(round(gpa, 1)) # round to the nearest tenth place

import math

print(math.pi)
print(math.sqrt(64)) # squareroot of 64
print(math.ceil(gpa))  # ceiling value
print(math.floor(gpa)) 

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incoorrect data
# zip_value = int("New York")