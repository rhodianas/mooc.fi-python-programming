# Write your solution here
number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
operation = input("Operation:")
if (operation == "add"):
    print(f"\n{number1} + {number2} = {number1+number2}")
if (operation == "multiply"):
    print(f"\n{number1} * {number2} = {number1*number2}")
if (operation == "subtract"):
    print(f"\n{number1} - {number2} = {number1-number2}")
