print("Sales Tax Calculate")
amount = float(input("Enter Purchase Amount: "))

calculate = amount * 0.06

tax = "{:.2f}".format(calculate)
print("Sales Tax is:" ,"{:.2f}".format(calculate))

