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
    if len(messnum) > len(keynum):
        keynum = keynum*(len(messnum)//len(keynum)+1)
        keynum = keynum[:len(messnum)]
    elif len(keynum) > len(messnum):
        keynum = keynum[:len(messnum)]
    print(messnum)
    print(len(messnum))
    print(keynum)
    print(len(keynum))
    emessnum = [x+(process*keynum[messnum.index(x)]) for x in messnum]
    print(emessnum)
    print(len(emessnum))
    emess = ''.join([associations[x%len(associations)] for x in emessnum])#PROBLEM????
    print(emess)

if process == "e":
    message = "David Wilson is amazing!!!"#input("Message: ")
    key = "3million"#input("Key: ")
    encrypt(message, key, 1)
elif process == "d":
    message = input("Message: ")
    key = "3million"#input("Key: ")
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
    if len(messnum) > len(keynum):
        keynumorig = keynum[:]
        keynum *= len(messnum)//len(keynum)
        keynum += keynumorig[:len(messnum)-len(keynum)]
    elif len(keynum) > len(messnum):
        keynum = keynum[:len(messnum)]
    emessnum = [x+(process*keynum[messnum.index(x)]) for x in messnum]
    emess = ''.join([associations[x%len(associations)] for x in emessnum])
    print(emess)

if process == "e":
    message = input("Message: ")
    key = input("Key: ")
    encrypt(message, key, 1)
elif process == "d":
    message = input("Message: ")
    key = input("Key: ")
    encrypt(message, key, -1)
elif process == "q":
    print("Goodbye!")
else:
    print("Did not understand command, try again.")
'''