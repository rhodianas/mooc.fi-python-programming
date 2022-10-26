# Write your solution here
limit = int(input("Upper limit:"))
base = int(input("Base:"))
number = 1
while number > 0 and number <= limit:
    print(number)
    number *= base
