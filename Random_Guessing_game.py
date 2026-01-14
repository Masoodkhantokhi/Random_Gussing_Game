import random

num = random.randint(1,11)

tries = 0

while True:
    guess = int(input(f"Enter your guess: "))
    if guess == num:
        tries += 1
        print(f"You guessed the Correct number in {tries} tries")
        break
    elif num < guess:
        print("Go a little lower")
        tries += 1
    elif num > guess:
        print("Go a little higher")
        tries += 1
    else:
        tries += 1
        print("You Guessed the wrong number")
