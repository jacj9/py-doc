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
######################

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
#####################

# import re

# # password = input("Enter a password: ")

# def is_password_valid(password):
#     if not len(password) >= 8:
#         return False
    
#     if not re.search(r'[a-z]', password): # At least one lower case letter
#         return False
    
#     if not re.search(r'[A-Z]', password): # At least one upper case letter
#         return False
    
#     if not re.search(r'[!@#$%^&*()_+\-=\[\]{};"\\|,.<>\/?~]', password): # At least one special character
#         return False
    
#     if not re.search(r'\d', password): # At lease one digit
#         return False
    
#     if re.search(r'\s', password): # No whitespace character
#         return False
    
#     return True

# print(is_password_valid("Blabl ebl1bl)blu")) # False
# print(is_password_valid("Abs123!s$"))  # True
# print(is_password_valid("123we3"))        # False
# print(is_password_valid("pA^sswo-rd_123")) # True

# if is_password_valid(password):
#     print("Valid password")
# else:
#     print("Not valid password")


#############################
"""
Create a simple password strength checker
Written on January 25, 2025
"""
# import re

# def password_strength(password):
#     if len(password) < 8:
#         return False
    
#     if not re.search('[a-z]', password):
#         return False
    
#     if not re.search('[A-Z]', password):
#         return False
    
#     if not re.search('\d', password):
#         return False
    
#     if not re.search('[!@#$%^&*()_+=<>?/{}]', password):
#         return False
    
#     return True

# print(password_strength("hakewm"))
# print(password_strength("hA2#k9090s"))
# print(password_strength("h kwnsoJL"))
# print(password_strength("0 234PassW0rd"))
# print(password_strength("weakpas"))


"""Write a Python program that defines a function and takes 
a password string as input and returns its SHA-256 hashed 
representation as a hexadecimal string.

With this code, passwords can be securely stored and authenticated 
by hashing them and storing only their hashed representation.
Written on: January 26, 2025"""

# import hashlib

# def hash_password(password):
#     # Encode the password as bytes
#     password_bytes = password.encode('utf-8')

#     # Use SHA-256 hash function to create a hash object
#     hash_object = hashlib.sha256(password_bytes)

#     # Get the hexadecimal representation of the hash
#     password_hash = hash_object.hexdigest()

#     return password_hash

# password = input("Input a password: ")
# hashed_password = hash_password(password)
# print("Your hashed password is: ", hashed_password)


####################
# Hashlib exercise. Similar to the previous exercise above.
# Written on: January 26, 2025
# import hashlib

# def hashed_password(password):
#     # Create a hash object using SHA-256
#     hash_object = hashlib.sha256(password.encode('utf-8'))

#     # Get the hexadecimal digest of the hash
#     hex_digest = hash_object.hexdigest()

#     return hex_digest

# print(hashed_password("hello world"))

##################################
# Generate a random password with a combination of uppercase and 
# lowercase letters, digits, and special characters.
# Written on: January 26, 2025

# import secrets
# import string

# def generate_password(length=12):
#     alphabet = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(secrets.choice(alphabet) for i in range(length))

# password = generate_password()
# print(password)

#### Another attempt ######
# import secrets
# import string

# def random_password(length=12):
#     alphabet = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(secrets.choice(alphabet) for i in range(length))

# print(random_password(20))


###########################################
# Write a Python program that defines a function and takes a password string 
# as input and returns its SHA-256 hashed representation as a hexadecimal string.
# Written on: January 27, 2025
###########################################
# import hashlib

# def hash_pass(password):
#     encode = password.encode('utf-8')

#     hash_object = hashlib.sha256(encode)

#     hex_digest = hash_object.hexdigest()

#     return hex_digest

# print("Your hashed password is ", hash_pass("Hello world"))
# print(hash_pass("January 27, 2025"))
# print(hash_pass("Extra practice"))


##################################
# Generate a random password with a combination of uppercase and 
# lowercase letters, digits, and special characters.
# Written on: January 27, 2025
###################################

# import random
# import string

# def generate_password(length=12):
#     # Define the characters to use in the password
#     alfabet = string.ascii_letters + string.digits + string.punctuation

#     # Use the random module to generate the password
#     password = r''.join(random.choice(alfabet) for i in range(length))

#     return password

# password_length_str = input("Input the desire length of your password: ")

# # Defaults to 12 characters password if there is no input
# if password_length_str:
#     password_length = int(password_length_str)
# else:
#     password_length = 12

# password = generate_password(password_length)
# print(f"Generated password is: {password}")


############################################
# Write a Python program to check if a password meets the following criteria:
# At least 8 characters long and
# Contains at least one uppercase letter, one lowercase letter, one digit, and 
# one special character (!, @, #, $, %, or &)
# If the password meets the criteria, print a message that says "Valid Password." 
# If it doesn't meet the criteria, print a message that says 
# "Password does not meet requirements."
# Written on: January 28, 2025
##############################################

import re

def valid_password(password):
    if len(password) < 8:
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'[!@#$%&]', password):
        return False
    
    return True

password = input('Input your passowrd: ')
is_valid = valid_password(password)

if is_valid:
    print("Valid Password")
else:
    print("Password does not meet requirements.")