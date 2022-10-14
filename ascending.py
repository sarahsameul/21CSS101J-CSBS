print("RA2211042010034")

def find_lowest(numberset):
    lowest = numberset[0]
    for number in numberset[1:]:
        if number < lowest:
            lowest = number

    return lowest


totalnos = int(input("Enter Total Numbers in Set: "))
listnos = []
for i in range(totalnos):
    num = int(input("Enter Number: "))
    listnos.append(num)

ascendingset = []
i = len(listnos)
listtosort = listnos
print('Unsorted List: ', listnos)

for item in range(i):
    numbertoinsert = find_lowest(listtosort)
    ascendingset.append(numbertoinsert)

    for k in range(len(listtosort)):

        if listtosort[k] == numbertoinsert:
            listtosort.pop(k)
            break


print('List Sorted in Ascending Order: ', ascendingset)
# print("Average of", totalnos, "numbers is: ",average)
