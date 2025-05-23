a=float(input("Enter the amount of the bill: "))
if a<=1000:
    print("Final amount: ", (a-(a*(10/100))))
elif a <= 5000:
    print("Final amount: ", (a - (a * (20 / 100))))
elif a<=10000:
    print("Final amount: ", (a-(a*(30/100))))
else:
    print("Final amount: ", (a-(a*(50/100))))
