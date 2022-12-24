def main():
    due = 50
    print("Amount Due: 50")
    paid = int(input("Insert Coin: "))

    while paid !=5 and paid != 10 and paid != 25:
        print("Amount Due: 50")
        paid = int(input("Insert Coin: "))

    print(f"Amount Due: {due - paid}")
    calculate(paid, due)

def calculate(paid, due):
    while paid < due:
        due = due - paid
        paid = int(input("Insert Coin: "))

        if due - paid == 0:
            print("Change Owed: 0")
        elif due > paid:
            print(f"Amount Due: {due - paid}")

    if paid > due:
        print(f"Change Owed: {paid - due}")

main()