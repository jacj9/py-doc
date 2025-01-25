# Simple python cybersecurity exercises
# Written on: January 23, 2025

# Scenario: You are building a simple Python script that asks the user to input 
# a password and checks if it meets certain security requirements.

# import re

# user_password = input("Please enter a password: ")

# def validate_password(user_password):
#     # Check the length of the password
#     if len(user_password) < 8:
#         return False
    
#     # Check for at least one uppercase letter
#     if not re.search(r'[A-Z]', user_password):
#         return False
    
#     # Check for at least one digit
#     if not re.search(r'\d', user_password):
#         return False
    
#     # Check for at least one special character
#     if not re.compile(r'[^a-zA-Z0-9]', user_password):
#         return False
    
#     return True

# if validate_password(user_password):
#     print("Your password is strong!")
# else:
#     print("Your password is weak. Please choose a stronger password.")


#####################
# Scenario: You are building a user registration form for a website. One of 
# the fields in the form is an email address. Your task is to validate 
# the user input and ensure that it is a properly formatted email address.

# import re

# # Test the validate_email function
# email1 = input("Please enter an email address: ")

# def validate_email(email1):
#     # Email pattern to check for the proper format
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
#     # Check if the email matches the pattern
#     if re.match(pattern, email1):
#             return True
#     else:
#             return False

# if validate_email(email1):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")


####################
## Password validation practice
# Written on: January 24, 2025

import re


password = input("Enter a password: ")

def is_password_valid(password):
    if not len(password) >= 8:
        return False
    
    if not re.search(r'[a-zA-Z]', password):
        return False
    
    if not re.search(r'[_!#^&]', password):
        return False
    
    if not re.search(r'[0-9]', password):
        return False
    
    return True

if is_password_valid(password):
    print("Valid password")
else:
    print("Not valid password")