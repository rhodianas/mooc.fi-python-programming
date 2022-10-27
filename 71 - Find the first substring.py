# Write your solution here
word = input("Please type in a word")
input_char = input("Please type in a character:")
char_exists = input_char in word
if char_exists:
    index = word.find(input_char)
    if index+3 <= len(word):
        print(word[index:index+3])
