cost_price = float(input("enter cost price:"))
sale_price = float(input("enter sale price:"))
if sale_price > cost_price:
    profit = sale_price - cost_price
    print("profit =", profit)
elif cost_price > sale_price:
    loss = cost_price - sale_price
    print("loss=", loss) 
else:
    print("no profit no loss")       