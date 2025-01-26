"""Python exercises without following a particular topic.
Written on: January 19, 2025"""

# ## 1. Swapping Values
# # Swap the values of two variables without using a temporary variable.
# x = 5
# y = 10

# x, y = y, x

# print("x is equal to ",x)
# print("y is equal to ", y)


# ## 2. Area of a Circle
# # Calculate the area of a circle given its radius
# radius = float(input("Enter the radius of the circles: "))
# radius2 = radius * radius
# pi = 3.14159
# area = pi * radius * radius
# area1 = pi * radius2

# print("The area of the circle is:", area)
# print("The area of the circle is:", area1)


# ## 3. Temperature Conversion
# # Convert Celsius to Fahrenheit
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32

# print("Temperature in Fahrenheit: ", fahrenheit)

# # Convert Fahrenheit to Celsius
# fahrenheit = float(input("Enter temperature in Fahrenheit: "))
# celsius = (fahrenheit - 32) * (5/9)

# print("Temperature in Celsius: ", celsius)


# ## 4. String Manipulation
# # Get a string from the user
# # Count the number of vowels in the string.
# string = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0

# for char in string:
#     if char in vowels:
#         count += 1

# print("Your string has ", count, "number of vowels.")


# ## 5. Data Type Conversion
# # Get user input for age and height
# # Conver age to an integer and height to a float.

# age = int(input("Enter your age: "))
# height = float(input("Enter your height in meters: "))

# print("Your age is: ", age)
# print("Your height is: ", height)


## 
# Write a function that takes a string as input and prints 
# each character on a new line. Try "hello"
# Written on: January 22, 2025

# input_string = str(input("Please enter a string: "))

# def print_character(input_string):
#     for letter in input_string:
#         print(letter)

# print_character("Hello ")
# print_character(input_string)

"""Draw a Tree
from video: https://youtube.com/shorts/SGD7k-8i0Mw?si=ex3097d5O10B6AiV
Written on January 25, 2025"""
#           *
#          ***
#         *****
#        *******
#       *********
#      *********** 11
#           *

# height = 6
# 6 * 2 = 12 - 1 = width of the tree

def tree(height):
    length = height * 2 - 1
    stars = 1 # starts with 1 star by default
    for i in range(1,height+1): # 
        print(("*" * stars).center(length))
        stars+=2 # increment 2 after printing each layer
    print("*".center(length))

tree(6)