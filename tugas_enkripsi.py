letters = "abcdefghijklmnopqrstuvwxyz "
invLetters = {}
numLetters = len(letters)

for i in range(numLetters):
        invLetters[letters[i]] = i

def encrypt(plain, cols, password):
        global letters,invLetters, numLetters
        cipher = ""
        cipher2 = ""

        numLines = len(plain)//cols
        if(numLines * cols) < len(plain):
        	numLines = numLines + (len(plain)%numLines)

        block = [[" " for i in range(cols)] for j in range(numLines)]   
        i = 0
        j = 0   

        for k in range(len(plain)):
        	block[i][j] = plain [k]
        	j = (j+1) % cols
        	if j == 0:
        		i = i+1
        for j in range(cols):
        	for i in range(numLines):
        		cipher = cipher+block[i][j]
                             
        passwordIndex = 0
        for i in range(len(cipher)):
                shift = invLetters[password[passwordIndex]]
                index = (invLetters[cipher[i]] + shift) % numLetters
                cipher2 = cipher2 + letters[index]
                passwordIndex = (passwordIndex + 1) % len(password)
        return cipher2

def decrypt(cipher2, cols, password):
        global letters,invLetters, numLetters
        plain = ""
        cipher = ""

        passwordIndex = 0
        for i in range(len(cipher2)):
                shift = invLetters[password[passwordIndex]]
                index = (invLetters[cipher2[i]] - shift) % numLetters
                cipher = cipher + letters[index]
                passwordIndex = (passwordIndex + 1) % len(password)

        numLines = len(cipher)//cols
        if(numLines * cols) < len(cipher):
                numLines = numLines + (len(cipher)%numLines)

        block = [[" " for i in range(numLines)] for j in range(cols)]

        i = 0
        j = 0

        for k in range(len(cipher)):
                block[j][i] = cipher [k]
                i = (i+1) % numLines
                if i == 0:
                        j = j+1
        for i in range(numLines):
                for j in range(cols):
                        plain = plain+block[j][i]

        return plain

plain = input("Plain text: ")
cols = int(input("Column number: "))
password = input("Password: ")

cipher = encrypt(plain, cols, password)
print ("Ciphered: " + cipher)
decipher = decrypt(cipher, cols, password)
print ("Deciphered: " + decipher)
