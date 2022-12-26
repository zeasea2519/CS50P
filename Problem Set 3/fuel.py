#convert fraction to percent
#if 1% or less, print E
#if 99% or more, print F

while True:
    try:
        frac = input("Fraction: ")
        num, den = frac.split("/")
        num = int(num)
        den = int(den)
        num / den
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        if num / den > 1:
            pass
        else:
            break

percent = round((num / den) * 100)

if percent >= 99:
    print("F")

elif percent <= 1:
    print("E")

else:
    print(f"{percent}%")