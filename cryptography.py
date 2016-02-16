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
    key = "hello"#input("Key: ")
    messnum = [associations.find(x) for x in message]
    keynum = [associations.find(x) for x in key]
    print(messnum)
    print(keynum)
    def evenlength(s, l):
        sorig = s[:]
        s *= len(l)//len(s)
        s += sorig[:len(l)-len(s)]
    if len(messnum) > len(keynum):
        evenlength(keynum, messnum)
    elif len(keynum) > len(messnum):
        evenlength(messnum, keynum)
    print(messnum)
    print(keynum)
    
elif process == "d":
    message = input("Message: ")
elif process == "q":
    print("Goodbye!")
else:
    print("Did not understand command, try again.")