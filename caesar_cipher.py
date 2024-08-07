import os
clear = lambda: os.system('cls')

#shift the message to the right
def shiftRight(message, nShift):
    encryptedMessage = ""
    for letter in message:
        if ord(str(letter)) >= 97 and ord(str(letter)) <= 122:
            encryptedMessage+= chr((ord(str(letter)) - 97 + nShift)%26 + 97)
        elif ord(str(letter)) >= 65 and ord(str(letter)) <= 90:
            encryptedMessage+= chr((ord(str(letter)) - 65 + nShift)%26 + 65)
        else:
            encryptedMessage += letter
    return encryptedMessage

#shift the message to the left
def shiftLeft(message, nShift):
    decryptedMessage = ""
    for letter in message:
        if ord(str(letter)) >= 97 and ord(str(letter)) <= 122:
            tempChar = (ord(str(letter)) - 97 - nShift)%26
            if tempChar < 0: tempChar = 26 - tempChar 
            
            decryptedMessage+= chr(tempChar+ 97)
            
        elif ord(str(letter)) >= 65 and ord(str(letter)) <= 90:
            tempChar = (ord(str(letter)) - 65 - nShift)%26
            if tempChar < 0: tempChar = 26 - tempChar 
            
            decryptedMessage+= chr(tempChar + 65)
        else:
            decryptedMessage += letter
    
    return decryptedMessage

#This function encrypts a plain text given nShift of input
def encrypt():
    encryptedMessage = ""
    clear()
    print("====================================")
    print("Caesar Ciper Encyrption")
    print("====================================")
    
    nShift = 0
    try:
        nShift = int(input("Shift Value: "))
    except:
        print("Invalid Input")
        return 1
    
    
    message = input("Message: ")
    print("====================================")
    print("Results:\n")
    
    
    if nShift > 0:
        encryptedMessage = shiftRight(message, nShift)
    elif nShift < 0:
        encryptedMessage = shiftLeft(message, abs(nShift))
    else:
        encryptedMessage += message
    
    
    print(encryptedMessage)
    print("====================================")
    input("Enter to continue...")


#This function decrypts a encrypted caesar cipher message given nShift of input
def decrypt():
    clear()
    decryptedMessage = ""
    clear()
    print("====================================")
    print("Caesar Ciper decryption")
    print("====================================")
    
    try:
        nShift = int(input("Shift Value: "))
    except:
        print("Invalid Input")
        return 1
    
    message = input("Encyrpted Message: ")
    print("====================================")
    print("Results:\n")
    
    if nShift > 0:
        decryptedMessage = shiftLeft(message, nShift)
    elif nShift < 0:
        decryptedMessage = shiftRight(message, abs(nShift))
    else:
        decryptedMessage += message
    
    print(decryptedMessage)
    print("====================================")
    input("Enter to continue...")


# This Function is the Main page of the code where users will be prompted to choose a action
def main():
    while True:
        print("====================================")
        print("Caesar Cipher")
        print("====================================")
        print("[1] Encrypt")
        print("[2] Decrypt")
        print("[3] Exit")
        print("====================================")
        op1 = input("Option: ")
        
        if op1 == "1":
            encrypt()
        elif op1 == "2":
            decrypt()
        elif op1 == "3":
            print("Exit!")
            break
        else:
            clear()
            print("Invalid Input!!")
    
   
    
if __name__ == "__main__":
    main()