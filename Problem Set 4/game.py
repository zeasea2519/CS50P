import random

while True:
    try:
        level = int(input("Level: "))

    except ValueError:
        continue

    if level > 0:
        break

    else:
        continue

number = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))

    except ValueError:
        continue

    if guess > number:
        print("Too large!")
        continue

    elif guess < number:
        print("Too small!")
        continue

    else:
        print("Just right!")
        break