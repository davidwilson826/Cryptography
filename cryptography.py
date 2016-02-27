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
    emess = [associations[x%len(associations)] for x in emess]
    print(emess)
    for x in emess[:-1]:
            print(x,end='')
    print(emess[-1])

if process == "e":
    message = "Hello, how are you?"#input("Message: ")
    key = "qwe712345"#input("Key: ")
    encrypt(message, key, 1)
elif process == "d":
    message = input("Message: ")
    key = "qwe712345"#input("Key: ")
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
    print(emess)
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
    emess = [sum(x) for x in zip(messnum, keynum)]
    print(emess)
    emess = ''.join([associations[x%len(associations)] for x in emess])
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