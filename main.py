
import math
import os

# use icon.png for a test
def encrypt(filename):
    file = open(filename, "rb")
    byteArray = bytearray(file.read())
    print(len(byteArray))
    
    f = lambda x : (x + len(byteArray) - 2)%256
    
    for i,v in enumerate(byteArray):
        byteArray[i] = f(v)
    file.close()

    writefile = open(filename, "wb")
    writefile.write(byteArray)
    writefile.close()

    return "successfully encrypted a file : " + filename

def decrypt(filename):
    file = open(filename, "rb")
    byteArray = bytearray(file.read())
    print(len(byteArray))
    f = lambda x : (x - len(byteArray) + 2)%256
    writefile = open(filename, "wb")
    for i,v in enumerate(byteArray):
        byteArray[i] = f(v)

    file.close()

    writefile = open(filename, "wb")
    writefile.write(byteArray)
    writefile.close()

    return "successfully decrypted a file : " + filename

def encryptAllFile():
    a = next(os.walk('.'))
    r = []
    if len(a) > 2:
        b = a[2]
    else:
        b = a[1]
    for i in b:
        if i != "main.py":
            r.append(encrypt(i))
    return r

def decryptAllFile():
    a = next(os.walk('.'))
    r = []
    if len(a) > 2:
        b = a[2]
    else:
        b = a[1]
    for i in b:
        if i != "main.py":
            r.append(decrypt(i))
    return r


if __name__ == "__main__":
    while True:
        
        option = input("(1. encrypt | 2. decrypt | 3. encrypt all files (current script folder) | 4. decrypt all files (current script folder)) : ")
        if option == "1":
            filename = input("filename: ")
            print(encrypt(filename))
        elif option == "2":
            filename = input("filename: ")
            print(decrypt(filename))
        elif option == "3":
            for i in encryptAllFile():
                print(i)
        elif option == "4":
            for i in decryptAllFile():
                print(i)
        else:
            print("please choose a number")
