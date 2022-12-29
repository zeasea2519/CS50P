#must have emoji module installed to work
#pip install emoji

import emoji

x = input("Input: ")
x = emoji.emojize(x, language="alias")
print("Output:" + x)