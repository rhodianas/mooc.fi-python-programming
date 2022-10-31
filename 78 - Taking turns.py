# Write your solution here
number = int(input("Please type in a number:"))
i = 1
while i <= number/2:
    print(i)
    print(number+1-i)
    i += 1
if number % 2 == 1:
    print(i)
