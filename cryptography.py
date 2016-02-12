"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

process = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if process == "e":
    message = input("Message: ")
    key = input("Key: ")
    messnum = [associations.find(x) for x in message]
    keynum = [associations.find(x) for x in key]
elif process == "d":
    message = input("Message: ")
elif process == "q":
    print("Goodbye!")
else:
    print("Did not understand command, try again.")