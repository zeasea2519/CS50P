greeting = input("Greeting: ")
greeting = greeting.lower()
greeting = greeting.strip()

if greeting.startswith("hello") == True:
    print("$0")

elif greeting.startswith("h") == True:
    print("$20")

else:
    print("$100")