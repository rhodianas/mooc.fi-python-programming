# Write your solution here
def line(length, text):
    if text == "":
        text = "*"
    text = text[0]
    while len(text) < length:
        text += text
    text = text[:length]
    print(text)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")
