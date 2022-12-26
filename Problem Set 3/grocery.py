items = {}
while True:
    try:
        item = input().upper()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1

    except EOFError:
        for x in sorted(items):
            print(items[x], x)
        break