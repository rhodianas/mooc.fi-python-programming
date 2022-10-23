# Write your solution here
first_string = input("Please type in the 1st word:")
second_string = input("Please type in the 2nd word:")
if first_string > second_string:
    print(f"{first_string} comes alphabetically last.")
elif first_string < second_string:
    print(f"{second_string} comes alphabetically last.")
elif first_string == second_string:
    print("You gave the same word twice.")
