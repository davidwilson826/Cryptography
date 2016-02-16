"""
cryptography.py
Author: <your name here>
Credit: http://stackoverflow.com/questions/1720421/how-to-append-list-to-second-list-concatenate-lists

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

process = "e"#input("Enter e to encrypt, d to decrypt, or q to quit: ")

if process == "e":
    message = "David Wilson"#input("Message: ")
    key = "hello3"#input("Key: ")
    messnum = [associations.find(x) for x in message]
    keynum = [associations.find(x) for x in key]
    keynumorig = keynum[:]
    print(messnum)
    print(keynum)
    while len(keynum) < len(messnum)+len(keynumorig):
        keynum += keynumorig
    keynum += keynumorig[:len(messnum)-len(keynum)]
    print(keynum)
    
elif process == "d":
    message = input("Message: ")
elif process == "q":
    print("Goodbye!")
else:
    print("Did not understand command, try again.")