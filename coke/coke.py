amount_due = 50
while amount_due > 0:
    x = int(input("Insert coin:"))
    if x == 25 or x == 10 or x == 5:
        amount_due -= x
    if amount_due > 0:
        print(f"Amount due: {amount_due}")
    elif amount_due < 0:
        print(f"Change owed: {-amount_due}")
        amount_due = 0
    else:
        print("Payment complete. Thank you!")
