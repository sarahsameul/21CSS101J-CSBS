print("RA2211042010034")

num = int(input("Enter Number: "))

factors = []
for i in range(1,num+1):
    if num%i == 0:
        factors.append(i)
    
print("Factors are:",factors)
