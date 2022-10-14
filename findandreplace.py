print("RA2211042010034")

inputstring = ""
chartofindandreplace = ""
chartoreplacewith = ""
replacedstring = ""

inputstring = input("Enter a string: ")
chartofindandreplace = input("Enter character to find and replace: ")
chartoreplacewith = input("Enter character to replace with: ")

for eachchar in list(inputstring):
    if eachchar == chartofindandreplace:
        replacedstring = replacedstring + chartoreplacewith
    else:
        replacedstring = replacedstring + eachchar

print("Input String is: ", inputstring)
print("Replaced String is: ", replacedstring)
