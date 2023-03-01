import random

word_list = ["nigger", "cunt", "pussy"]
word = list(word_list[random.randint(0, 2)])
guesses = [] 
guess_number = 0

for letter in word:
    guesses.append("_")
    
def check():
    global guess_number
    is_right = False
    for i, letter in enumerate(word):
        if letter == guess:
            is_right = True
            guesses[i] = guess
    if is_right == False:
        guess_number += 1

def win():
    for letter in guesses:
        if letter == "_":
            return False
    return True

while not win():
    if guess_number >= 6:
        print('You got hanged')
        break
    guess = input("Type a letter\n")
    check()
    print(guesses, guess_number)
