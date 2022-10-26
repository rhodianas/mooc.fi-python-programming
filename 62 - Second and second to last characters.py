# Write your solution here
string = input("Please type in a string:")
if string[1] == string[-2]:
    character = string[1]
    print(f"The second and the second to last characters are {character}")
else:
    print("The second and the second to last characters are different")
