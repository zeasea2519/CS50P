def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)

    #no punctuation allowed
    if s.isalnum() == False:
        return False

    #length must be 2-6 characters
    elif len(s) < 2 or len(s) > 6:
        return False

    #must start with 2 letters
    elif s[0].isdigit() == True or s[1].isdigit() == True:
        return False

    #numbers must be at the end
    for i in range(len(s)): #
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    #first number cannot be 0
    for i in s:
        if i.isdigit():
            if int(i)==0:
                return False
            else:
                break

    return True


main()
