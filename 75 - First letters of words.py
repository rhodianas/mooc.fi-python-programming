# Write your solution here
sentence = input("Please type in a sentence:")
print(sentence[0])
space = " "
while space in sentence:
    i = sentence.find(space)
    if (i+1 < len(sentence)):
        print(sentence[i+1])
        sentence = sentence[i+1:]
