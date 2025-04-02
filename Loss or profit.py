actual_cost = float(input("pleasr enter the actual produt price: "))
sale_amount = float(input("please enter the Sales amount: "))

if (sale_amount>actual_cost) :
    amount = sale_amount-actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("no profit!!!")