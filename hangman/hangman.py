import random
from hangman_art import stages
from hangman_words import word_list

word = list(word_list[random.randint(0, len(word_list))])
guesses = [] 
lives = 6

for letter in word:
    guesses.append("_")
    
def check():
    global lives
    is_right = False
    for i, letter in enumerate(word):
        if letter == guess:
            is_right = True
            guesses[i] = guess
    if is_right == False:
        lives -= 1

def win():
    for letter in guesses:
        if letter == "_":
            return False
    return True

while not win():
    if lives <= 0:
        print('You got hanged! The word was ' + ''.join(word) + '!')
        break
    guess = input("Guess a letter\n").lower()
    check()
    print(guesses, stages[lives])
