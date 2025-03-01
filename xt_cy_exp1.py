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
    
#     if not re.search('\W', password):
#         return False
    
#     if not re.search('[!@#$%^&*()_+=<>?/{}]', password):
#         return False
    
#     return True

# print(password_strength("hakewm"))
# print(password_strength("hA2#k9090s"))
# print(password_strength("h kwnsoJL"))
# print(password_strength("0 234PassW0rd{"))
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

# import re

# def valid_password(password):
#     if len(password) < 8:
#         return False
    
#     if not re.search(r'[a-z]', password):
#         return False
    
#     if not re.search(r'[A-Z]', password):
#         return False
    
#     if not re.search(r'\d', password):
#         return False
    
#     if not re.search(r'[!@#$%&]', password):
#         return False
    
#     return True

# password = input('Input your passowrd: ')
# is_valid = valid_password(password)

# if is_valid:
#     print("Valid Password")
# else:
#     print("Password does not meet requirements.")


###################################################
# Write a Python function that takes a password as input and 
# returns a list of common character substitutions that 
# could be used to create a stronger password.
# Written on: January 29, 2025
################################################
# Practice attempt

# password = input("Input your password: ")

# def get_password_variants(password):
#     pass_variants = []
#     substitutions = {
#         'a': ['@', '4', 'A'],
#         'e': ['3', 'E'],
#         'i': ['1', '!', 'I'],
#         'o': ['0', '0'],
#         's': ['$', '5', 'S'],
#         't': ['7', 'T'],
#         'z': ['2', 'Z']
#     }

#     for i in range(len(password)):
#         if password[i] in substitutions: # Checks whether the character at the current index i of the password exists as a key in the substitutions dictionary
#             for sub in substitutions[password[i]]: # iterates over each element in the list of substitution
#                 pass_variant = password[:i] + sub + password[i+1:] # concatenation
#                 pass_variants.append(pass_variant) # adds generated password variant to the pass_variants list

#     pass_variants.append(password + '!')
#     pass_variants.append(password + '123')
#     pass_variants.append(password + '@')
#     pass_variants.append(password + '#')
#     pass_variants.append(password + '$')
#     pass_variants.append(password + '%')
#     pass_variants.append(password + '&')
#     pass_variants.append(password + '*')
#     pass_variants.append(password + '-')
#     pass_variants.append(password + '_')
#     pass_variants.append(password + '=')
#     pass_variants.append(password + '+')  
#     return pass_variants # Returns the pass_variants list

# result_variants = get_password_variants(password)
# print(result_variants)

#########
### Attempt no.2: February 1, 2025
#########

# password = input("Input your password: ")

# def alt_password(password):
#     # Creates an empty list to input pass_variant
#     variants = []
#     # A substitution dictionary list to substitute each character
#     substitutions = {
#         'a': ['@', '4', 'A'],
#         's': ['3', 'E', '#'],
#         'd': ['I', '1', '|'],
#         'f': ['0', 'O', 'Q', '*'],
#         'j': ['U', '()', '##']
#     }

#     for i in range(len(password)):
#         if password[i] in substitutions:
#             for sub in substitutions[password[i]]:
#                 pass_variant = password[:i] + sub + password[i+1:]
#                 variants.append(pass_variant)
    
#     variants.append(password + 'l4l4l4')
#     variants.append(password + '@9876')
#     variants.append(password + '$A$P')
#     variants.append('--__--'+ password +'****')
#     return variants

# is_variant = alt_password(password)
# print(is_variant)


####################################
# Write a Python function that reads a file containing a list of passwords, one per line.
# It checks each password to see if it meets certain requirements(e.g. at least 8 characters,
# contains both uppercase and lowercase letters, and at least one number and one special
# character.) Passwords that satisfy the requirements should be printed by the program.
# Written on: February 2, 2025
##################################
# For reference
# import re
# def check_password(password):
#     # Define regular expressions for each requirement
#     length_regex = re.compile(r'^.{8,}$')
#     uppercase_regex = re.compile(r'[A-Z]')
#     lowercase_regex = re.compile(r'[a-z]')
#     digit_regex = re.compile(r'\d')
#     special_regex = re.compile(r'[\W_]')
    
#     # Check if password meets each requirement
#     length_check = length_regex.search(password)
#     uppercase_check = uppercase_regex.search(password)
#     lowercase_check = lowercase_regex.search(password)
#     digit_check = digit_regex.search(password)
#     special_check = special_regex.search(password)
    
#     # Return True if all requirements are met, False otherwise
#     if length_check and uppercase_check and lowercase_check and digit_check and special_check:
#         return True
#     else:
#         return False

# # Open file containing passwords
# with open('passwords.txt') as f:
#     # Read each password from file and check if it meets requirements
#     for password in f:
#         password = password.strip()  # Remove newline character
#         if check_password(password):
#             print("Valid Password: "+password)
#         else:
#             print("Invalid Password: "+password)

###################
# Practice session
# Written on: February 6, 2025
####################

# import re

# def pass_requirements(password):
#     # Define regular expression for each requirement
#     len_re = re.compile(r'^.{8,}$')
#     cap_re = re.compile(r'[A-Z]')
#     low_re = re.compile(r'[a-z]')
#     num_re = re.compile(r'\d')
#     spec_re = re.compile(r'[\W_]')

#     # Ensure passwords meet the requirements
#     len_meet = len_re.search(password)
#     cap_meet = cap_re.search(password)
#     low_meet = low_re.search(password)
#     num_meet = num_re.search(password)
#     spec_meet = spec_re.search(password)

#     # If all of the requirements are met, return true, if not, returnFalse
#     if len_meet and cap_meet and low_meet and num_meet and spec_meet:
#         return True
#     else:
#         return False

# with open('passwords.txt') as f:
#     for password in f:
#         password = password.strip()
#         if pass_requirements(password):
#             print("Valid password: "+ password)
#         else:
#             print("Invalid password: " + password)


####################################################
# Write a Python program that reads a file containing 
# a list of usernames and passwords, one pair per line (separatized by a comma). 
# It checks each password to see if it has been leaked in a data breach. You can 
# use the "Have I Been Pwned" API (https://haveibeenpwned.com/API/v3) to check if a 
# password has been leaked.
######################################################
# import requests
# import hashlib

# # Read the file containing usernames and passwords
# with open('passwords.txt', 'r') as f:
#     for line in f:
#         # Split the line into username and password
#         username, password = line.strip().split(',')

#         # Hash the password using SHA-1 algorith
#         password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

#         # Make a request to "Have I Been Pwned" API to check if the password has been leaked
#         response = requests.get(f'https://api.pwnedpasswords.com/range/{password_hash[:5]}')

#         # If the response status code is 200, it means the password has been leaked
#         if response.status_code == 200:
#             # Get the list of hashes of leaked passwords that start with the same 5 character as the input password
#             hashes = [line.split(':') for line in response.text.splitlines()]

#             # Check if the hash of the input password matches any of the leaked password hashes
#             for h, count in hashes:
#                 if password_hash[5:] == h:
#                     print(f"Password for user {username} has been leaked {count} times.")
#                     break
#         else:
#             print(f"Could not check password for user {username}.")


##########################################
# Practicing the above exercise on my own
# Written on: February 9, 2025
#########################################


# import requests
# import hashlib

# with open('passwords.txt', 'r') as f:
#     for line in f:
#         username, password = line.strip().split(',')

#         password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

#         response = requests.get(f'https://api.pwnedpasswords.com/range/{password_hash[:5]}')

#         if response.status_code == 200:
#             hashes = [line.split(':') for line in response.text.splitlines()]

#             for h, count in hashes:
#                 if password_hash[5:] == h:
#                     print(f"Password for user {username} has been leaked {count} times.")
#                     break
#         else:
#             print(f"Could not check password for user {username}")


############################################################
# 6. Write a function check_password_strength(password) that takes 
# a password as input and returns a string indicating the strength 
# of the password based on the following criteria:
# "Weak": Less than 6 characters or only contains lowercase letters or only contains digits.
# "Average": At least 6 characters and contains a mix of uppercase and lowercase letters.
# "Strong": At least 8 characters and contains a mix of uppercase and lowercase letters, 
# digits, and special characters.
# Written on: February 13, 2025
#################################################################

## AI Answer key

# def check_password_strength(password):
#     password_length = len(password)

#     if password_length < 6:
#         return "Weak"
#     elif password_length >= 6:
#         if any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char.isdigit() for char in password) and any(char in '!@#$%^&*()_+' for char in password):
#             return "Strong"
#         else:
#             return "Average"
#     elif password_length >= 8:
#         if any(char.isalpha() for char in password) and any(char.isdigit() for char in password):
#             return "Average"

# password1 = "p123"
# password2 = "MyPass123"
# password3 = "MyP@ssw0rd!"

# print(check_password_strength(password1))
# print(check_password_strength(password2))
# print(check_password_strength(password3))


#################################################
# Practice the above exercise
# Written on: February 15, 2025
#################################################

# def check_password_strength(password):
#     password_length = len(password)

#     if password_length < 8:
#         return "Weak"
#     if password_length >=8:
#         if any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isalpha() for char in password) and any(char in '!@#$%^&*()_+' for char in password) and any(char.isdigit() for char in password):
#             return "Strong"
#         else:
#             return "Average"
    
# password1 = "p123"
# password2 = "MyPass123&"
# password3 = "MyP@ssw0rd!"

# print(check_password_strength(password1))
# print(check_password_strength(password2))
# print(check_password_strength(password3))


#######################################################
# Practice exercise 6 above
# Written on: February 18, 2025
#######################################################
# import re

# def check_password_strength(password):

#     if len(password) < 8:
#         return 'Weak'
#     if len(password) >=8:
#         if re.search(r'\d', password) and re.search(r'[a-z]', password) and re.search(r'[A-Z]', password) and re.search(r'[!@#$%^&*()_+=-]', password):
#             return 'Strong'
#         else:
#             return 'Average'

# password = 'abcd'
# password2 = 'Ab34%^J(jl)'
# password3 = 'ABNCCDKL90'

# print(check_password_strength(password))
# print(check_password_strength(password2))
# print(check_password_strength(password3))


###########################################################
# 7. Write a Python program that creates a password strength meter. The program should prompt 
# the user to enter a password and check its strength based on criteria such as length, complexity, 
# and randomness. Afterwards, the program should provide suggestions for improving the password's 
# strength.

# The highest strength password that meets the criteria specified in the program will receive 
# a score of 5.
# (e.g. at least 8 characters, contains both uppercase and lowercase letters, and at least 
# one number and one special character).

# Written on: February 17, 2025
################################################################

###################################
## Practice Exercise
## Written on: February 17, 2025
###################################
# import re
# def check_password_strength(password):
#     score = 0
#     suggestions = []
    
#     password_length = len(password)
      
#     # check for password length
#     if password_length >= 8:
#         score += 1
#     else:
#         suggestions.append("Password should be at least 8 characters long")

#     # check for uppercase letter
#     if re.search(r'[A-Z]', password):
#         score += 1
#     else:
#         suggestions.append("Password should contain at lease one uppercase letter")

#     #check for lowercase letter
#     if re.search(r'[a-z]', password):
#                score += 1
#     else:
#         suggestions.append("Password should contain at least one lowercase letter")

#     # check for numeric digit
#     if re.search(r'\d', password):
#         score += 1
#     else:
#         suggestions.append("Password should contain a numeric digit")

#     # check for special characters
#     if re.search(r'[!@#$%^&*()_+]', password):
#         score += 1
#     else:
#         suggestions.append("Password should contain at lease one  special character")
    
#     if score == 5:
#          suggestions.append("Strong password")
#     return score, suggestions

# password = 'password1234'
# password2 = 'Pass123#$$%'
# password3 = '#n23K'
# print(check_password_strength(password))
# print(check_password_strength(password2))
# print(check_password_strength(password3))


## Sample Solution

# import re

# def check_password_strength(password):
#     score = 0
#     suggestions = []

#     # check length
#     if len(password) >= 8:
#         score += 1
#     else:
#         suggestions.append("Password should be at least 8 characters long")

#     # check for uppercase letter
#     if re.search(r"[A-Z]", password):
#         score += 1
#     else:
#         suggestions.append("Password should contain at least one uppercase letter")

#     # check for lowercase letter
#     if re.search(r"[a-z]", password):
#         score += 1
#     else:
#         suggestions.append("Password should contain at least one lowercase letter")

#     # check for numeric digit
#     if re.search(r"\d", password):
#         score += 1
#     else:
#         suggestions.append("Password should contain at least one numeric digit")

#     # check for special character
#     if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#         score += 1
#     else:
#         suggestions.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)")

#     return score, suggestions
# password = input("Input a password: ")
# print(check_password_strength(password))


######################################################
# 8. Write a Python program that generates a password 
# using a random combination of words from a dictionary file.
# Written on: February 21, 2025
########################################################

## Answer key: Sample solution
# import random

# def generate_password():
#     with open('passwords2.txt') as f:

#         words = f.read().splitlines()
        
#     password = random.sample(words, 4)

#     password = "-".join(password)
    
#     return password

# password = generate_password()
# print(password)

##################################################
# Practice exercise 8
# February 22, 2025
##################################################

# import random

# # Open the dictionary file and read its content. You can use open() and read()
# with open('passwords2.txt', 'r') as f:
#     for line in f:
#         # Split the content into individual words. You can use the split() method.
#         my_list = f.read().strip() + "-"
#         random_words = random.sample(my_list, 4)
#         # print(random_words)
#         # print(my_list, random_words)
#         # for r in my_list:
#         #     print(r)
#         result = my_list.join(random_words)
#         print(result)


#########################################
# Practice exercise 8
# February 23, 2025
#########################################

# import random

# def generate_password():
#     with open('passwords2.txt') as f:
#         words = f.read().splitlines()

#     password = random.sample(words, 6)

#     password = "-".join(password)

#     return password

# password = generate_password()
# print(password)


"""
9. Write a Python program that simulates a dictionary attack on a password by 
trying out a list of commonly used passwords and their variations.
Written on: February 24, 2025
"""

import hashlib
# List of commonly used passwords and their variations
common_passwords = ["password", "password123", "letmein", "qwerty", "123456", "abc123", "admin", "welcome", "monkey", "sunshine"]
password_variations = ["", "123", "1234", "12345", "123456", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "<", ">"]
# Hash of the password to be attacked
hash_password = hashlib.sha256(b"password123").hexdigest()
# Try out all possible combinations of common passwords and their variations
for password in common_passwords:
    for variation in password_variations:
        possible_password = password + variation
        hash_combinations_password = hashlib.sha256(possible_password.encode()).hexdigest()
        if hash_combinations_password == hash_password:
            print(f'Password {possible_password} has been found')
            break
    else:
         continue
    break
else:
    print("Password not found")