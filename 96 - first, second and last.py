# Write your solution here
def first_word(text):
    index = text.find(" ")
    return text[:index]


def second_word(text):
    index = text.find(" ")
    text = text[index+1:]
    if " " in text:
        index = text.find(" ")
        return text[:index]
    return text


def last_word(text):
    while " " in text:
        index = text.find(" ")
        text = text[index+1:]
    return text


# You can test your function by calling it within the following block
if __name__ == "__main__":
    #sentence = "once upon a time there was a programmer"
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
