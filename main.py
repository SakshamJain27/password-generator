import random

upper = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
lower = "abcdefghigklmnopqrstuvwxyz"
numbers = "1234567890"
characters = "!@#$%^&*(){}|:?"

passcode = upper+lower+numbers+characters

length = int(input("Enter the length of the password"))

print("".join(random.sample(passcode, length)))
