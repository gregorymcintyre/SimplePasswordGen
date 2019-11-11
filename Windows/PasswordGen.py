import random
import string
#from tkinter import Tk

def randomStringwithDigitsAndSymbols(stringLength=16):
    """Generate a random string of letters, digits and special characters """

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

print("Generating Random String password with letters, digits and special characters \n")
#print (randomStringwithDigitsAndSymbols() )

pwds = []
#r = Tk()

for x in range(10):
	pwds.append(randomStringwithDigitsAndSymbols(16))

for x in range(10):
	print(str(x) + ". " + pwds[x])

#choice = input("\nChoose password number: ")
#r.withdraw()
#r.clipboard_clear()
#r.clipboard_append(pwds[int(choice)])
#r.update()
#r.destroy()
#print("Password copied to clipboard!")

input("\nPress enter to exit")

