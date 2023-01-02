def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            num, den = fraction.split("/")
            num = int(num)
            den = int(den)
            percentage = (num / den) * 100

            if num > den:
                fraction = input("Fraction: ")

            return int(percentage)

        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError


def gauge(percentage):
    if percentage >= 99:
        return("F")

    elif percentage <= 1:
        return("E")

    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()
