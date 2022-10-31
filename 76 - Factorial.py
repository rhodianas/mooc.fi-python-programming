# Write your solution here
while True:
    number = int(input("Please type in a number:"))
    if number <= 0:
        break
    else:
        factorial = i = 1
        while i <= number:
            factorial *= i
            i += 1
        print(f"The factorial of the number {number} is {factorial}")
        continue
print("Thanks and bye!")
