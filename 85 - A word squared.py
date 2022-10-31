# Write your solution here
def squared(input_text, number):
    i = 0
    text = ""
    while i < number:
        while len(text) < number:
            text += input_text
        print(text[0:number])
        text = text[number:]
        i += 1


# Testing the function
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
