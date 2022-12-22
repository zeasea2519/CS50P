expression = input("Expression: ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)

if y == "+":
    ans = x + z
    ans = round(ans, 1)
    print(ans)

elif y == "-":
    ans = x - z
    ans = round(ans, 1)
    print(ans)

elif y == "*":
    ans = x * z
    ans = round(ans, 1)
    print(ans)

elif y == "/":
    ans = x / z
    ans = round(ans, 1)
    print(ans)