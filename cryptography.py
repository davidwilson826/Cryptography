"""
cryptography.py
Author: David Wilson
Credit: http://stackoverflow.com/questions/1720421/how-to-append-list-to-second-list-concatenate-lists

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

process = "e"#input("Enter e to encrypt, d to decrypt, or q to quit: ")

if process == "e":
    message = "David Wilson"#input("Message: ")
    key = "hello!3"#input("Key: ")
    messnum = [associations.find(x) for x in message]
    keynum = [associations.find(x) for x in key]
    print(messnum)
    print(keynum)
    if len(messnum) > len(keynum):
        keynumorig = keynum[:]
        keynum *= len(messnum)//len(keynum)
        keynum += keynumorig[:len(messnum)-len(keynum)]
    elif len(keynum) > len(messnum):
        keynum = keynum[:len(messnum)]
    print(messnum)
    print(keynum)
    emessnum = [x+keynum[messnum.index(x)] for x in messnum]
    print(emessnum)
    emess = ''.join([associations[x%len(associations)] for x in emessnum])
    print(emess)
    
elif process == "d":
    message = input("Message: ")
elif process == "q":
    print("Goodbye!")
else:
    print("Did not understand command, try again.")
