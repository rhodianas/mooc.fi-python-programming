# Write your solution here
my_list = []
print(f"The list is now {my_list}")
item = 1
choice = ""
while choice != "x":
    choice = input("a(d)d, (r)emove or e(x)it:")
    if choice == "d":
        my_list.append(item)
        print(f"The list is now {my_list}")
        item += 1
    elif choice == "r":
        item -= 1
        my_list.remove(item)
        print(f"The list is now {my_list}")
    elif choice == "x":
        print("Bye!")
        break
    else:
        continue
