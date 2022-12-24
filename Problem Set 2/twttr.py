#not a massively elegant solution, but hey, it works

words = input("Input: ")
words = words.strip()

words = words.replace("i", "")
words = words.replace("e", "")
words = words.replace("o", "")
words = words.replace("a", "")
words = words.replace("u", "")
words = words.replace("I", "")
words = words.replace("E", "")
words = words.replace("O", "")
words = words.replace("A", "")
words = words.replace("U", "")

print("Output:", words)