# Write your solution here
my_list = []
item = int(input("New item:"))
while item != 0:
    my_list.append(item)
    print(f"The list now: {my_list}")
    print(f"The list in order: {sorted(my_list)}")
    item = int(input("New item:"))
print("Bye!")
