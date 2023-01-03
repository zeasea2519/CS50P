import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments.")

elif len(sys.argv) > 2:
    sys.exit("Not enough command-line arguments.")

elif (sys.argv[1]).endswith(".py") == False:
    sys.exit("Not a python file.")

else:
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.read().splitlines()
            total = len(lines)
            for line in lines:
                line = line.strip()
                if line.startswith("#") == True:
                    total = total - 1
                elif len(line) == 0:
                    total = total - 1
            print(total)
    except FileNotFoundError:
        sys.exit("File does not exist.")
