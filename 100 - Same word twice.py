# Write your solution here
my_list = []
while True:
    word = input("Word:")
    if word in my_list:
        break
    my_list.append(word)
total = len(my_list)
print(f"You typed in {total} different words")
