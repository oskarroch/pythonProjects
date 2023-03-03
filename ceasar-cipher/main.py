from alphabet import alphabet
from art import logo

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    arr = list(text)
    for i, letter in enumerate(arr):
        if alphabet.index(letter) + shift >= len(alphabet):
            shift_num = (alphabet.index(letter) - len(alphabet)) + shift
        else:
            shift_num = alphabet.index(letter) + shift
        arr[i] = alphabet[shift_num]
    encoded = ''.join(arr)
    print(f"The encoded text is {encoded}")

def decrypt(text, shift):
    arr = list(text)
    for i, letter in enumerate(arr):
        if alphabet.index(letter) - shift < 0:
            shift_num = (alphabet.index(letter) + len(alphabet)) - shift
        else:
            shift_num = alphabet.index(letter) - shift
        arr[i] = alphabet[shift_num]
    decrypted = ''.join(arr)
    print(f"The decrypted text is {decrypted}")


if direction == 'encode':
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print('there is no such direction')
