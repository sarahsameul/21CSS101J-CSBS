print("RA2211042010034")

num1 = int(input("Enter First Number: "))
op = input("Enter Operator: ")
num2 = int(input("Enter Second Number: "))
if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid Operator") 
