from string import ascii_uppercase
from itertools import cycle

alphabet = list(ascii_uppercase) + [",", ".", "-", "_"]
#message = 'SIU_CS-Department_is_the_best'
#key = 'Carbondale'

message = raw_input('Enter message: ')
key = raw_input('Enter key: ')


blockSize = len(key)

def encrypt(message, key):
	cipher = ''
	for m, k in zip(message, cycle(key)):
		index = alphabet.index(m) + alphabet.index(k)		
		cipher += alphabet[index % 30]
	return cipher

def decrypt(cipher, key):
	decrypt = ''
	for m, k in zip(cipher, cycle(key)):
		index = alphabet.index(m) - alphabet.index(k)		
		decrypt += alphabet[index % 30]
	return decrypt


def main():
	cipher  = encrypt(message.upper(), key.upper())
	total_key = key + cipher[0:blockSize]
	print ('Encryption')
	print ('Plaintext:  ',  message)
	print ('Key: ', total_key)
	print ('Cipher: ',  cipher)
	cipher_ = decrypt(cipher, key.upper())
	print('Decryption')
	print ('Cipher:  ',  cipher)
	print ('Key: ', total_key)
	print ('Decrypt: ',  cipher_)

main()
