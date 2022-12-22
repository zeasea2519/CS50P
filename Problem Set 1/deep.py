ans = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
ans = ans.strip()
ans = ans.lower()

match ans:
    case "forty-two" | "42" | "forty two":
        print("Yes")

    case _:
        print("No")