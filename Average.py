totalnos = int(input("Enter Total Numbers in Set: "))
listnos = []
for i in range(0,totalnos):
    num = int(input("Enter Number: "))
    listnos.append(num)
total = 0
for number in listnos:
    total = total + number

average = total/totalnos
print("Average of", totalnos, "numbers is: ",average)
