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
    print(messnum)
    print(keynum)
    emess = [sum(x) for x in zip(messnum, keynum)]
    print(emess)
    charnum = 0
    while charnum < len(emess):
        char = emess[charnum]%len(associations)
        print(char)
        if char == 70:
            emess[charnum] = "\\"
        else:
            emess[charnum] = associations[char]
        charnum += 1
    emess = ''.join(emess)
    print(emess)

if process == "e":
    message = "ZeroDivisionError: division by zero"#input("Message: ")
    key = "asdfg123"#input("Key: ")
    encrypt(message, key, 1)
elif process == "d":
    message = input("Message: ")
    key = "asdfg123"#input("Key: ")
    encrypt(message, key, -1)
elif process == "q":
    print("Goodbye!")
else:
    print("Did not understand command, try again.")
    
'''
Back-up:

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

process = input("Enter e to encrypt, d to decrypt, or q to quit: ")

def encrypt(message, key, process):
    messnum = [associations.find(x) for x in message]
    keynum = [associations.find(x) for x in key]
    keynum = keynum*(len(messnum)//len(keynum))+keynum[:len(messnum)%len(keynum)]
    keynum = [process*x for x in keynum]
    print(messnum)
    print(keynum)
    emessnum = [sum(x) for x in zip(messnum, keynum)]
    print(emessnum)
    emess = ''.join([associations[x%len(associations)] for x in emessnum])
    print(emess)

if process == "e":
    message = "ZeroDivisionError: division by zero"#input("Message: ")
    key = "asdfg123"#input("Key: ")
    encrypt(message, key, 1)
elif process == "d":
    message = input("Message: ")
    key = "asdfg123"#input("Key: ")
    encrypt(message, key, -1)
elif process == "q":
    print("Goodbye!")
else:
    print("Did not understand command, try again.")
'''