#!/usr/bin/env python3

import random
import string

def randomStringwithDigitsAndSymbols(stringLength=16):
    """Generate a random string of letters, digits and special characters """

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

print("Generating Random String password with letters, digits and special characters ")
print (randomStringwithDigitsAndSymbols() )
print (randomStringwithDigitsAndSymbols(16) )
print (randomStringwithDigitsAndSymbols(16) )
print (randomStringwithDigitsAndSymbols(16) )
print (randomStringwithDigitsAndSymbols(16) )
print (randomStringwithDigitsAndSymbols(16) )
print (randomStringwithDigitsAndSymbols(16) )
print (randomStringwithDigitsAndSymbols(16) )
print (randomStringwithDigitsAndSymbols(16) )
print (randomStringwithDigitsAndSymbols(16) )

input("Press enter to exit")
