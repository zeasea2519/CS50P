import random


def main():
    level = get_level()
    questions = 0
    score = 0
    while questions < 10:
        x, y = generate_integer(level)
        attempts = 3
        while attempts > 0:
            ans = int(input(f"{x} + {y} = "))
            if ans == (x + y):
                score = score + 1
                break
            else:
                print("EEE")
                attempts = attempts - 1
                if attempts == 0:
                    print(x, "+", y, "=", x+y)
                    break
                else:
                    continue

        questions = questions + 1
    print("Score:", score)

def get_level():
    level = input("Level: ")

    if level.isalpha() or int(level) <= 0 or int(level) > 3:
        input("Level: ")
    else:
        level = int(level)
        for i in [1,2,3]:
            if level == i:
                return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)

    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)

    else:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x, y


if __name__ == "__main__":
    main()
