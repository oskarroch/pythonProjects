from alphabet import alphabet
from encode import encrypt 
from decode import decrypt
from art import logo

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print('there is no such direction')
