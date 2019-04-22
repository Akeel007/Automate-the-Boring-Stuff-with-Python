#! python3
# Strong Password detection with Regexes
import re

# Strength Checks
charRegex = re.compile(r'(\w{8,})')  # Check if password has atleast 8 characters
lowerRegex = re.compile(r'[a-z]+') # Check if at least one lowercase letter
upperRegex = re.compile(r'[A-Z]+')# Check if atleast one upper case letter
digitRegex = re.compile(r'[0-9]+') # Check if at least one digit.

# Enter password text
passwordText = input('Enter Password: ') # Enter password text 

''' TODO: Enter conditions to see if password passes all checks and then return
a message if it does.'''
if charRegex.findall(passwordText) == []:  # Checks if the password does not contain 8 characters and returns a message
    print('Password must contain atleast 8 characters')
elif lowerRegex.findall(passwordText)==[]: # Checks if the password does not contain a lowercase character and returns a message
    print('Password must contain atleast one lowercase character')
elif upperRegex.findall(passwordText)==[]: # Checks if the password does not contain an uppercase character and returns a message
    print('Password must contain atleast one uppercase character')
elif digitRegex.findall(passwordText)==[]: # Checks if the password does not contain a digit character and returns a message
    print('Password must contain atleast one digit character')
else:  # if the above 4 conditions are successfully passed, pringt out a message saying the password is strong.
    print('Your password is strong. Good job!')
