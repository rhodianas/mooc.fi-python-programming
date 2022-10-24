# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum = 0
positives = 0
negatives = 0
while True:
    number = int(input("Number:"))
    if number == 0:
        break
    else:
        count += 1
        sum += number
        if number > 0:
            positives += 1
        else:
            negatives += 1
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {float(sum)/count}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")
