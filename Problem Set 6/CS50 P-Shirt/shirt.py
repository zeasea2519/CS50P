import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments.")

elif len(sys.argv) > 3:
    sys.exit("Not enough command-line arguments.")

elif (sys.argv[1]).endswith(".png") == False and (sys.argv[1]).endswith(".jpg") == False and (sys.argv[1]).endswith(".jpeg") == False:
    sys.exit("Not an image file.")

elif not ((sys.argv[1]).endswith(".png") and (sys.argv[2]).endswith(".png")) and not ((sys.argv[1]).endswith(".jpg") and (sys.argv[2]).endswith(".jpg")) and not ((sys.argv[1]).endswith(".jpeg") and (sys.argv[2]).endswith(".jpeg")):
    sys.exit("Input and output have different extensions.")

else:
    shirt = Image.open("shirt.png")
    try:
        picture = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist.")
    else:
        cropped = ImageOps.fit(picture, shirt.size)
        cropped.paste(shirt, mask=shirt)
        cropped.save(sys.argv[2])