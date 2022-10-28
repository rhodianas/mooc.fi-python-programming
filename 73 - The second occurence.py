# Write your solution here
input_string = input("Please type in a string:")
substring = input("Please type in a substring:")
if len(input_string) >= 3 and substring != "":
    index = input_string.find(substring)
    if substring in input_string and index+len(substring) <= len(input_string):
        input_string = input_string[index+len(substring):]
        second_index = input_string.find(substring)
        if substring in input_string and second_index+len(substring) <= len(input_string):
            print(
                f"The second occurrence of the substring is at index {index+second_index+len(substring)}.")
        else:
            print("The substring does not occur twice in the string.")
    else:
        print("The substring does not occur twice in the string.")
