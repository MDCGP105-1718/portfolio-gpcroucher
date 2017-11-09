import os
import csv
import random
with open("words.txt") as wordfile:
    reader = csv.reader(wordfile, delimiter=" ")
    wordlist = list(reader)
wordlist_length = len(wordlist[0])
print(wordlist, wordlist_length)

def script(): # main script loop
    lives = 9
    players = int(input("How many players? "))
    if players == 2:
        while True:
            word = str(input("Enter the word: ")).strip().lower() # takes input for word as a string and removes leading and trailing whitespace
            if " " in word: # if word contains a space
                print("Words may not contain spaces.")
                continue # doesn't exit loop
            if not word.isalpha():
                print("Words must contain only letters.")
                continue # doesn't exit loop
            else:
                break # exits loop
    elif players == 1:
        word = wordlist[0][random.randint(0, wordlist_length)]

    guessed_characters = []

    os.system("cls") # clears the terminal
    clue = "_" * len(word) # constructs a clue with underscores
    while lives > 0:
        print(clue) # show letters correctly guessed along with gaps
        guess = str(input("Make a guess: ")).strip().lower() # takes in a guess, discarding whitespace
        if len(guess) != 1: # if guess is not a single character
            print("Single characters only please.")
            continue # back to prompt
        if not guess.isalpha(): # if guess is not an alphabetic character
            print("Letters only please.")
            continue # back to prompt
        if guess in guessed_characters: # if guess already guessed
            print("You already guessed this!")
            continue # back to prompt
        guessed_characters.append(guess) # add to list of guessed characters
        if guess not in word: # if guess is wrong
            lives -= 1 # lose a life (starts at 9)
            print(pic[lives]) # print the corresponding hanged man
            if lives <= 0:
                print("You have died!")
                break # end game
            else:
                continue # back to prompt
        for i in findOccurences(word, guess): # for every occurence of guess in word
            s = list(clue) # cast clue as string to s as list
            s[i] = guess # replaces the underscore at the relevant index with the guess
            clue = "".join(s) # replace clue with new clue, casting to string
        if clue == word: # win condition
            print("You win!") # congratulate user
            return True
    return

def findOccurences(s, ch): # https://stackoverflow.com/a/13009866
    return [i for i, letter in enumerate(s) if letter == ch] # returns a list of indexes in the source string which match a given letter

pic = [
"""
   _____
   |    o
   |   /|\\
   |   / \\
-------""",
"""
   _____
   |    o
   |   /|\\
   |   /
-------""",
"""
   _____
   |    o
   |   /|\\
   |
-------""",
"""
   _____
   |    o
   |   /|
   |
-------""",
"""
   _____
   |    o
   |    |
   |
-------""",
"""
   _____
   |    o
   |
   |
-------""",
"""
   _____
   |
   |
   |
-------""",
"""

   |
   |
   |
-------""",
"""
-------""",
""
]

while True:
    script()
