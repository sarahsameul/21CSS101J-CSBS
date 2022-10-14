print("RA2211042010034")

a = input("Would You Like To Convert To INR or USD? ")
if a == "INR":
    INR = int(input("Enter Amount In USD: "))
    USD = round(INR*82)
    print("Amount In INR Is",USD)
if a == "USD":
    inr = int(input("Enter Amount In INR: "))
    usd = round(inr/82)
    print("Amount In USD Is",usd)
