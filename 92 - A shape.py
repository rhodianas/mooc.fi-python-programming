# Copy here code of line function from previous exercise and use it in your solution
def line(length, text):
    if text == "":
        text = "*"
    text = text[0]
    while len(text) < length:
        text += text
    text = text[:length]
    print(text)


def shape(width, triangle_filler, height, rectangle_filler):
    i = 1
    while i <= width:
        line(i, triangle_filler)
        i += 1
    i = 0
    while i < height:
        line(width, rectangle_filler)
        i += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
