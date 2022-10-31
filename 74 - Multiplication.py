# Write your solution here
number = int(input("Please type in a number:"))
i = 1
while True:
    j = 1
    while True:
        print(f"{i} x {j} = {i*j}")
        j += 1
        if j > number:
            break
    i += 1
    if i > number:
        break
