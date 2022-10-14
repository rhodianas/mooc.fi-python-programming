# Write your solution here
students = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))
groups_formed = (students//group_size)
if (students % group_size) > 0:
    groups_formed += 1
print(f"Number of groups formed: {groups_formed}")
