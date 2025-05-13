# Ask for the total bill amount
bill_amount = float(input("Enter the total bill amount (in $): "))

# Ask how much the customer paid
amount_paid = float(input("Enter the amount paid by the customer (in $): "))

# Calculate the due or change
if amount_paid > bill_amount:
    change = amount_paid - bill_amount
    print(f"Customer has overpaid. Return ${change:.2f} as change.")
elif amount_paid < bill_amount:
    due = bill_amount - amount_paid
    print(f"Customer still owes ${due:.2f}.")
else:
    print("Bill is paid in full. No dues. All settled! ")
