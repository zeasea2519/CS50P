def main():
    greeting = input("Greeting: ")
    amount = value(greeting)
    print(f"${amount}")


def value(greeting):
    greeting = greeting.lower()
    greeting = greeting.strip()
    if greeting.startswith("hello") == True:
        return(0)

    elif greeting.startswith("h") == True:
        return(20)

    else:
        return(100)


if __name__ == "__maitestn__":
    main()
