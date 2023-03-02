from alphabet import alphabet

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
