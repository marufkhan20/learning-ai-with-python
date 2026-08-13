import random

ranNum = random.randint(1, 10)

tries = 0

while True:
    guess = int(input("Please Guess Your Number Between 1 - 10: "))

    if ranNum == guess:
        tries += 1
        print(f"You're right you guessed the number is {tries} tries")
        break;

    else:
        tries += 1
        print("Sorry you're wrong!")