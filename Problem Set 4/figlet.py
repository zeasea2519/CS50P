#must have pyfiglet installed to work
#pip install pyfiglet

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    selectedfont = figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(text))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] in fonts:
        text = input("Input: ")
        selectedfont = figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid Usage")
else:
    sys.exit("Invalid Usage")