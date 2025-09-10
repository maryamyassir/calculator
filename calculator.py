'''
    CALCULATOR APP
Basic features
    - adding two numbers
    - subtracting two numbers
    - multiplying two numbers
    - dividing two numbers

More features (later)
    - remembering the previous answer
    - +/- button
    - square
    - square root

'''
# variables
num1 = 0
num2 = 0
total = 0


# getting the user to use the calculator
function = input("What would you like to do?\nAdd [A]\nSubtract [S]\nMultiply [M]\nDivide [D]\n\n")

if (function == "A"):
    num1 = int(input("1st Number: "))
    num2 = int(input("2nd Number: "))
    total = num1 + num2
    print(total)

if (function == "S"):
    num1 = int(input("1st Number: "))
    num2 = int(input("2nd Number: "))
    total = num1 - num2
    print(total)

if (function == "M"):
    num1 = int(input("1st Number: "))
    num2 = int(input("2nd Number: "))
    total = num1 * num2
    print(total)

if (function == "D"):
    num1 = int(input("1st Number: "))
    num2 = int(input("2nd Number: "))
    total = num1 / num2
    print(total)