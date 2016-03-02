"""
cryptography.py
Author: David Wilson
Credit: http://stackoverflow.com/questions/1720421/how-to-append-list-to-second-list-concatenate-lists,
http://www.decalage.info/en/python/print_list

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

process = input("Enter e to encrypt, d to decrypt, or q to quit: ")

def encrypt(message, key, process):
    messnum = [associations.find(x) for x in message]
    keynum = [associations.find(x) for x in key]
    keynum = keynum*(len(messnum)//len(keynum))+keynum[:len(messnum)%len(keynum)]
    keynum = [process*x for x in keynum]
    emess = [sum(x) for x in zip(messnum, keynum)]
    print(emess)
    emess = ''.join([associations[x%len(associations)] for x in emess])
    print(emess)

if process == "e":
    message = 'How now? A rat? Dead, for a ducat, dead!'#input("Message: ")
    key = '123456'#input("Key: ")
    encrypt(message, key, 1)
elif process == "d":
    message = input("Message: ")
    key = '123456'#input("Key: ")
    encrypt(message, key, -1)
elif process == "q":
    print("Goodbye!")
else:
    print("Did not understand command, try again.")