# Write your solution here
input_string = input("Please type in a string:")
vowel = "aeo"
i = 0
while i < len(vowel):
    if vowel[i] in input_string:
        print(f"{vowel[i]} found")
    else:
        print(f"{vowel[i]} not found")
    i += 1
