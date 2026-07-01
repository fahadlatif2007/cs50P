amount_due = 50
while amount_due > 0:
    payment = int(input("How much would you like to pay? "))
    amount_due -= payment
    if amount_due > 0:
        print(f"Amount due: {amount_due}")
    elif amount_due < 0:
        print(f"Change owed: {-amount_due}")
        amount_due = 0
    else:
        print("Payment complete. Thank you!")
