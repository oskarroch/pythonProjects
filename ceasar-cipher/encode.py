from alphabet import alphabet

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
