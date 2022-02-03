
import math

# use icon.png for a test
def encrypt(filename):
    file = open(filename, "rb")
    byteArray = bytearray(file.read())
    
    f = lambda x : (x + len(byteArray) - 2)%256
    
    for i,v in enumerate(byteArray):
        byteArray[i] = f(v)
    file.close()

    writefile = open(filename, "wb")
    writefile.write(byteArray)
    writefile.close()

    return "successfully encrypted a file"

def decrypt(filename):
    file = open(filename, "rb")
    byteArray = bytearray(file.read())
    f = lambda x : (x - len(byteArray) + 2)%256
    writefile = open(filename, "wb")
    for i,v in enumerate(byteArray):
        byteArray[i] = f(v)

    file.close()

    writefile = open(filename, "wb")
    writefile.write(byteArray)
    writefile.close()

    return "successfully decrypted a file"

if __name__ == "__main__":
    while True:
        filename = input("filename: ")
        option = input("(1. encrypt | 2. decrypt) : ")
        if option == "1":
            
            print(encrypt(filename))
        elif option == "2":
            
            print(decrypt(filename))
        else:
            print("please choose 1 or 2")
