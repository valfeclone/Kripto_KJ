letters = "abcdefghijklmnopqrstuvwxyz "
invLetters = {}

numLetters = len(letters)

for i in range(numLetters):
	invLetters[letters[i]] = i

def encrypt(plain, shift):
	global letters, invLetters, numLetters
	cipher = ""
	for i in range(len(plain)):
		index = (invLetters[plain[i]] + shift) % numLetters
		cipher = cipher + letters[index]
	return cipher

def decrypt(cipher, shift):
        global letters, invLetters, numLetters
        plain = ""
        for i in range(len(plain)):
                index = (invLetters[cipher[i]] - shift) % numLetters
                plain = plain + letters[index]
        return plain

plain = input("Enter plain text: ")
shift = input("Input shift number: ")

shift = int(shift)

cipher = encrypt(plain, shift)
print ("Cipher: " + cipher)


cipher = input("Enter cipher text: ")
shift = input("Input shift number: ")

shift = int(shift)

plain = decrypt(plain, shift)
print ("Plain text: " + plain)

