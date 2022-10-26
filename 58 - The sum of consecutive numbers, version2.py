# Write your solution here
limit = int(input("Limit:"))
num = 1
sum = 1
consecutive_sum = f"The consecutive sum: {num} "
while sum < limit:
    num += 1
    sum += num
    consecutive_sum += f"+ {num} "
consecutive_sum += f"= {sum}"
print(consecutive_sum)
