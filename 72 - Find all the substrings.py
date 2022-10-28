# Write your solution here
word = input("Please type in a word:")
input_char = input("Please type in a character:")
index = word.find(input_char)
if word != "" and input_char != "":
    while index+3 <= len(word) and input_char in word:
        print(word[index:index+3])
        word = word[index+1:]
        index = word.find(input_char)
