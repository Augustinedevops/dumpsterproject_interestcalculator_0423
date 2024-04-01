outstanding, rate, payment = 1000.000, 0.005, 100.0
interest = 0
for month in range(1, 15):
    if outstanding + interest > payment:
        interest = outstanding * rate
        balance = outstanding + interest - payment
        print(month, outstanding, interest, payment, balance)
        outstanding = balance
    else:
        print("at the ", month, "month, please pay" ,balance)
        break
