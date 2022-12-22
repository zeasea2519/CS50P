#i did very strongly base this off someone else's solution online as i simply wasn't sure how to implement exact hours
#like 14:00 without getting a float division by 0 error

def main():
    exp = input('What time is it? ')
    exp = exp.strip()
    t = convert(exp)
    if 7 <= t <= 8:
        print('breakfast time')
    elif 12 <= t <= 13:
        print('lunch time')
    elif 18 <= t <= 19:
        print('dinner time')
    else:
        pass



def convert(time):
    if time.find(' ') != -1:
        t, p = time.split()
        h, m = t.split(':')
    else:
        h, m = time.split(':')
        p = 'not set'
    try:
        h = int(h)
        m = int(m)
    except ValueError:
        quit('Invalid format')
    else:
        if p == 'p.m.':
            return 12 + h + m / 60
        return h + m / 60



if __name__ == "__main__":
    main()