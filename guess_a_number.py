import random

guesses = 0
hasWon = False
target = random.randint(1,20)

player_name = input("What's your name?\n")
print("Guess a number between 1 and 20")

while guesses < 6:
    print("Take a guess: ")
    userGuess = None
    try:
        userGuess = int(input())
    except:
        print("Please guess a valid number")
        continue
    if userGuess < target:
        print("Guess was too low")
        guesses += 1
    elif userGuess > target:
        print("Guess was too high")
        guesses += 1
    else:
        print(f'Congratulations, {player_name}, you have won the game in {guesses} tries!')
        hasWon = True
        break

if hasWon == False:
    print("You lose")