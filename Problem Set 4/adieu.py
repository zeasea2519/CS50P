#must have inflect module installed to work
#pip install inflect

import inflect
p = inflect.engine()

names = []

while True:
    try:
        x = input("Name: ")
        names.append(x)

    except EOFError:
        break

adieulist = p.join(names)
print("Adieu, adieu, to " + adieulist)