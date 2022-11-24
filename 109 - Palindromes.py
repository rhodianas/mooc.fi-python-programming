# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(string):
    return string == string[::-1]


while (True):
    string_input = input("Please type in a palindrome:")
    if palindromes(string_input):
        print(f"{string_input} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
