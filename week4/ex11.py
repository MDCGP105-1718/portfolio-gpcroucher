from random import randint

def checkguess(guess, target):
    if guess == target:
        return True
    elif guess < target:
        print("Guess higher!")
        return False
    elif guess > target:
        print("Guess lower!")
        return False

target = randint(1, 100)

guesscounter = 0
success = False
while success == False:
    guesscounter += 1
    guess = int(input("Make a guess! (1 - 100) "))
    success = checkguess(guess, target)

print("Correct! It took you", guesscounter, "guesses.")
