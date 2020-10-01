def encrypt(plain, cols):
	cipher = ""
	numLines = len(plain)//cols
	print("Numlines: " + str(numLines))
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
	return cipher

def decrypt(cipher, cols):
        plain = ""
        numLines = len(cipher)//cols
        if(numLines * cols) < len(cipher):
                numLines = numLines + (len(plain)%numLines)

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

plain = input ("Plain text: ")
cols = input ("Cols: ")
cols = int(cols)

cipher = encrypt(plain, cols)
print ("Cipher: " + cipher)
plain = decrypt(cipher, cols)
print ("Plain: " + plain)

