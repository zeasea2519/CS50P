def main():
    word = input("Input: ")
    word = word.strip()
    word = shorten(word)
    print("Output:", word)


def shorten(word):
    word = word.replace("i", "")
    word = word.replace("e", "")
    word = word.replace("o", "")
    word = word.replace("a", "")
    word = word.replace("u", "")
    word = word.replace("I", "")
    word = word.replace("E", "")
    word = word.replace("O", "")
    word = word.replace("A", "")
    word = word.replace("U", "")
    return word


if __name__ == "__main__":
    main()
